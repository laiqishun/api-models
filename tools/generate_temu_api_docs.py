from __future__ import annotations

import copy
import hashlib
import json
import re
import shutil
from collections import OrderedDict, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(r"D:\workspace\sp-api-models\api-models")
OUT = ROOT / "temu-api"

SOURCES = {
    "cn_dict": Path(r"C:\Users\Administrator\Downloads\Temu CN 数据字典(1).md"),
    "cn": Path(r"C:\Users\Administrator\Downloads\Temu CN API文档.md"),
    "us": Path(r"C:\Users\Administrator\Downloads\Temu美国本土API文档.md"),
    "eu": Path(r"C:\Users\Administrator\Downloads\Temu欧洲本土API文档.md"),
    "eu_add": Path(r"C:\Users\Administrator\Downloads\Temu欧洲API文档新增接口-0416.md"),
    "global": Path(r"C:\Users\Administrator\Downloads\Temu全球API文档.md"),
}

API_RE = re.compile(r"^(?:bg|temu)(?:\.[A-Za-z0-9]+){2,}$")
API_TOKEN_RE = re.compile(r"\b(?:bg|temu)\.[A-Za-z0-9_.]+\b")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

COMMON_REQUEST_PARAMS = [
    {
        "name": "type",
        "type": "STRING",
        "required": True,
        "description": "API type. For Temu router APIs this is the operation name, for example bg.order.list.v2.get.",
    },
    {"name": "app_key", "type": "STRING", "required": True, "description": "Application key."},
    {"name": "access_token", "type": "STRING", "required": True, "description": "Seller authorization token."},
    {
        "name": "timestamp",
        "type": "STRING",
        "required": True,
        "description": "UNIX timestamp in seconds. Temu docs state it should be within 300 seconds before or after current time.",
    },
    {"name": "sign", "type": "STRING", "required": True, "description": "Request signature."},
    {"name": "data_type", "type": "STRING", "required": False, "description": "Optional response data format; Temu docs use JSON."},
    {"name": "version", "type": "STRING", "required": False, "description": "API version. Most docs default to V1."},
]

CN_GROUP_MAP = {
    "PA网关调用说明": ("partner-gateway-api", "PA Gateway"),
    "货品API组": ("product-api", "Product"),
    "货品API组-PA": ("product-api-pa", "Product PA"),
    "库存管理API组": ("inventory-api", "Inventory"),
    "库存管理API组-PA": ("inventory-api-pa", "Inventory PA"),
    "图片处理API组": ("image-processing-api", "Image Processing"),
    "说明书API组": ("instruction-file-api", "Instruction File"),
    "说明书API组-PA": ("instruction-file-api-pa", "Instruction File PA"),
    "类目属性API组": ("category-attribute-api", "Category Attribute"),
    "类目属性API组-PA": ("category-attribute-api-pa", "Category Attribute PA"),
    "视频上传API组": ("video-upload-api", "Video Upload"),
    "尺码表API组": ("size-chart-api", "Size Chart"),
    "尺码表API组-PA": ("size-chart-api-pa", "Size Chart PA"),
    "商品模特试穿API组": ("model-fitting-api", "Model Fitting"),
    "寄样/质检/退供API组": ("sample-quality-return-api", "Sample Quality Return"),
    "备货及发货API组": ("stock-shipping-api", "Stock And Shipping"),
    "运单标签&箱唛": ("waybill-box-label-api", "Waybill And Box Label"),
    "商品条码API组-PA": ("product-barcode-api-pa", "Product Barcode PA"),
    "销售API组": ("sales-api", "Sales"),
    "活动API组": ("marketing-activity-api", "Marketing Activity"),
    "基础API组": ("authorization-api", "Authorization"),
    "基础API组-PA": ("authorization-api-pa", "Authorization PA"),
    "编辑API组": ("product-edit-api", "Product Edit"),
    "编辑API组-PA": ("product-edit-api-pa", "Product Edit PA"),
    "申报价/核价/调价API": ("price-review-api", "Price Review"),
    "申报价/核价/调价API-PA": ("price-review-api-pa", "Price Review PA"),
    "活动API组-PA": ("marketing-activity-api-pa", "Marketing Activity PA"),
    "JIT组": ("jit-api", "JIT"),
    "JIT组-PA": ("jit-api-pa", "JIT PA"),
}

REGION_GROUP_MAP = {
    "authorization": ("authorization-api", "Authorization"),
    "product": ("product-api", "Product"),
    "price": ("price-api", "Price"),
    "order": ("order-api", "Order"),
    "logistics": ("logistics-api", "Logistics"),
    "fulfillment": ("fulfillment-api", "Fulfillment"),
    "return and refund": ("return-refund-api", "Return And Refund"),
    "return and rufund": ("return-refund-api", "Return And Refund"),
    "promotion": ("promotion-api", "Promotion"),
    "tax": ("tax-api", "Tax"),
}

REGION_META = {
    "temu-cn-api": {
        "title": "Temu CN API",
        "description": "China cross-border Temu APIs, including current CN gateway operations and PA gateway replacements.",
        "sourceKey": "cn",
        "defaultGateway": "/openapi/router",
        "defaultGatewayNote": "CN source tables state /openapi/router. Use the CN host configured for the seller application.",
    },
    "temu-us-api": {
        "title": "Temu US Local API",
        "description": "Temu local seller API for US local stores.",
        "sourceKey": "us",
        "defaultGateway": "https://openapi-b-us.temu.com/openapi/router",
    },
    "temu-eu-api": {
        "title": "Temu EU Local API",
        "description": "Temu local seller API for European local stores. Includes the 0416 logistics scanform additions.",
        "sourceKey": "eu",
        "defaultGateway": "https://openapi-b-eu.temu.com/openapi/router",
    },
    "temu-global-api": {
        "title": "Temu Global Local API",
        "description": "Temu local seller API for non-US Americas and other global local-store regions covered by the global document.",
        "sourceKey": "global",
        "defaultGateway": "https://openapi-b.temu.com/openapi/router",
    },
}

STOP_LABELS = {"收起", "Show Less", "Copy", "Switch color", "Json", "JSON", "CURL", "Curl"}

DICT_ANCHORS = {
    "skuClassification": ("半托管发品sku分类必传的叶子类目", "skuClassification leaf-category list"),
    "classId": ("尺码表分类", "size-chart classId/className mapping"),
    "className": ("尺码表分类", "size-chart classId/className mapping"),
    "region2Id": ("发品-省份枚举值", "province enum for product origin"),
    "provinceCode": ("发品-省份枚举值", "province enum for addresses"),
    "bindSiteIds": ("半托管站点列表", "semi-managed siteId list"),
    "siteId": ("半托管站点列表", "siteId list"),
    "siteIds": ("半托管站点列表", "siteId list"),
    "siteIdList": ("半托管站点列表", "siteId list"),
    "semiManagedSiteMode": ("半托管站点列表", "semi-managed pan-EU/non-pan-EU site mode"),
    "productName": ("货品名称长度限制规则", "product name length limits by category"),
    "netContentNumber": ("净含量必填叶子类目", "net-content required leaf categories"),
    "shipmentLimitSecond": ("承诺发货时效说明", "promised shipping time values"),
    "modelId": ("部分类目模特信息必填", "model information requirements"),
    "modelType": ("部分类目模特信息必填", "model information requirements"),
    "modelFeature": ("部分类目模特信息必填", "model information requirements"),
    "firstType": ("定制品定制工艺层级关系", "customization first-level process enum"),
    "twiceType": ("定制品定制工艺层级关系", "customization second-level process enum"),
    "isBasePlate": ("支持底板套板的类目", "base-plate supported categories"),
}

DICT_DESC_PATTERNS = [
    (re.compile(r"省份|region2Id|provinceCode", re.I), ("发品-省份枚举值", "province enum")),
    (re.compile(r"站点|siteId|bindSiteIds", re.I), ("半托管站点列表", "siteId list")),
    (re.compile(r"承诺发货|shipmentLimitSecond", re.I), ("承诺发货时效说明", "promised shipping time values")),
    (re.compile(r"货品名称|productName", re.I), ("货品名称长度限制规则", "product name length limits")),
    (re.compile(r"净含量|netContent", re.I), ("净含量必填叶子类目", "net-content requirements")),
    (re.compile(r"尺码表|classId|className", re.I), ("尺码表分类", "size-chart class mapping")),
    (re.compile(r"模特", re.I), ("部分类目模特信息必填", "model information requirements")),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def clean_cell(value: str) -> str:
    value = value.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    value = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", value)
    value = re.sub(r"\[([^\]]+)\]\(([^)]*)\)", r"\1", value)
    value = value.replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", value).strip()


def api_tokens(value: str) -> list[str]:
    visible = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value).replace(" ", "")
    return [token.rstrip(".") for token in API_TOKEN_RE.findall(visible) if token.count(".") >= 2]


def operation_filename(api_type: str) -> str:
    return api_type.replace("/", "_") + ".json"


def schema_name(api_type: str, suffix: str) -> str:
    return api_type.replace(".", "_").replace("-", "_") + suffix


def temu_type_to_schema(raw_type: str | None) -> OrderedDict:
    raw = (raw_type or "").strip()
    upper = raw.upper().replace(" ", "")
    schema = OrderedDict()

    if upper.endswith("[]"):
        item_type = raw[:-2]
        schema["type"] = "array"
        schema["items"] = temu_type_to_schema(item_type)
    elif upper in {"LIST", "ARRAY"}:
        schema["type"] = "array"
        schema["items"] = {"type": "object"}
    elif upper in {"OBJECT", "MAP", "HASHMAP", "JSON"}:
        schema["type"] = "object"
        schema["additionalProperties"] = True
    elif upper in {"INTEGER", "INT"}:
        schema["type"] = "integer"
        schema["format"] = "int32"
    elif upper in {"LONG"}:
        schema["type"] = "integer"
        schema["format"] = "int64"
    elif upper in {"DOUBLE", "FLOAT", "DECIMAL", "NUMBER", "BIGDECIMAL"}:
        schema["type"] = "number"
    elif upper in {"BOOLEAN", "BOOL"}:
        schema["type"] = "boolean"
    else:
        schema["type"] = "string"

    if raw:
        schema["x-temu-type"] = raw
    return schema


def merge_parameter_rows(*groups: list[OrderedDict]) -> list[OrderedDict]:
    rows = []
    for group in groups:
        rows.extend(group or [])
    return rows


def parameter_rows_to_schema(rows: list[OrderedDict], api_type: str | None = None) -> OrderedDict:
    schema = OrderedDict()
    schema["type"] = "object"
    schema["additionalProperties"] = True
    properties = OrderedDict()
    required = []
    seen = set()

    for row in rows:
        name = str(row.get("name", "")).strip()
        if not name or name == "$item" or name in seen:
            continue
        seen.add(name)
        prop = temu_type_to_schema(row.get("type"))
        if row.get("description"):
            prop["description"] = row["description"]
        if row.get("offlineReference"):
            prop["x-temu-offline-reference"] = row["offlineReference"]
            if row.get("offlineReferenceReason"):
                prop["x-temu-offline-reference-reason"] = row["offlineReferenceReason"]
        if name == "type" and api_type:
            prop["enum"] = [api_type]
            prop["default"] = api_type
            if prop.get("description"):
                prop["description"] = prop["description"] + f" Must be `{api_type}` for this operation."
            else:
                prop["description"] = f"Must be `{api_type}` for this operation."
        properties[name] = prop
        if row.get("required") is True and name not in required:
            required.append(name)

    if api_type:
        if "type" not in properties:
            properties["type"] = OrderedDict(
                [
                    ("type", "string"),
                    ("enum", [api_type]),
                    ("default", api_type),
                    ("description", f"Must be `{api_type}` for this operation."),
                ]
            )
        if "type" not in required:
            required.insert(0, "type")

    schema["properties"] = properties
    if required:
        schema["required"] = required
    return schema


def swagger_gateway_parts(gateway_url: str) -> tuple[str | None, str | None, str]:
    if gateway_url.startswith("http://") or gateway_url.startswith("https://"):
        parsed = urlparse(gateway_url)
        return parsed.scheme, parsed.netloc, parsed.path or "/openapi/router"
    return None, None, gateway_url if gateway_url.startswith("/") else "/" + gateway_url


def operation_to_swagger(operation: OrderedDict) -> OrderedDict:
    api_type = operation["apiType"]
    operation_id = operation["operationId"]
    request_def = schema_name(api_type, "Request")
    response_def = schema_name(api_type, "Response")
    gateway_url = operation.get("gateway", {}).get("url", "/openapi/router")
    scheme, host, router_path = swagger_gateway_parts(gateway_url)

    request_rows = merge_parameter_rows(operation.get("commonParameters", []), operation.get("requestParameters", []))
    response_rows = operation.get("responseParameters", [])
    request_schema = parameter_rows_to_schema(request_rows, api_type=api_type)
    response_schema = parameter_rows_to_schema(response_rows)

    swagger = OrderedDict()
    swagger["swagger"] = "2.0"
    swagger["info"] = OrderedDict(
        [
            ("title", f"{operation['group']['title']} - {api_type}"),
            ("description", operation.get("description") or operation.get("title") or api_type),
            ("version", operation.get("lastUpdateTime") or "1.0"),
        ]
    )
    if host:
        swagger["host"] = host
    if scheme:
        swagger["schemes"] = [scheme]
    swagger["consumes"] = ["application/json"]
    swagger["produces"] = ["application/json"]
    swagger["basePath"] = "/"

    post = OrderedDict()
    post["tags"] = [operation["group"]["title"]]
    post["operationId"] = operation_id
    post["summary"] = operation.get("title") or api_type
    post["description"] = operation.get("description") or operation.get("title") or api_type
    post["parameters"] = [
        OrderedDict(
            [
                ("name", "body"),
                ("in", "body"),
                ("required", True),
                ("description", f"Temu router request body. The `type` field must be `{api_type}`."),
                ("schema", {"$ref": f"#/definitions/{request_def}"}),
            ]
        )
    ]
    post["responses"] = OrderedDict(
        [
            (
                "200",
                OrderedDict(
                    [
                        ("description", "Temu API response."),
                        ("schema", {"$ref": f"#/definitions/{response_def}"}),
                    ]
                ),
            )
        ]
    )
    post["x-temu-api-type"] = api_type
    post["x-temu-region-module"] = operation.get("regionModule")
    post["x-temu-group"] = operation.get("group")
    post["x-temu-gateway"] = operation.get("gateway")
    if operation.get("endpointTable"):
        post["x-temu-endpoint-table"] = operation["endpointTable"]
    if operation.get("audience"):
        post["x-temu-audience"] = operation["audience"]
    if operation.get("lastUpdateTime"):
        post["x-temu-last-update-time"] = operation["lastUpdateTime"]
    post["x-temu-common-parameters"] = operation.get("commonParameters", [])
    post["x-temu-request-parameters"] = operation.get("requestParameters", [])
    post["x-temu-response-parameters"] = operation.get("responseParameters", [])
    if operation.get("rateLimiting"):
        post["x-temu-rate-limiting"] = operation["rateLimiting"]
    if operation.get("additionalTables"):
        post["x-temu-additional-tables"] = operation["additionalTables"]
    if operation.get("examples"):
        post["x-temu-examples"] = operation["examples"]
    if operation.get("source"):
        post["x-temu-source"] = operation["source"]
    if operation.get("migration"):
        post["x-temu-migration"] = operation["migration"]
    if operation.get("alternateApiTypes"):
        post["x-temu-alternate-api-types"] = operation["alternateApiTypes"]
    if operation.get("schemaCopiedFromLegacyType"):
        post["x-temu-schema-copied-from-legacy-type"] = operation["schemaCopiedFromLegacyType"]
    if operation.get("synthetic"):
        post["x-temu-synthetic"] = True
    if operation.get("deduplicatedSources"):
        post["x-temu-deduplicated-sources"] = operation["deduplicatedSources"]

    swagger["paths"] = OrderedDict([(router_path, OrderedDict([("post", post)]))])
    swagger["definitions"] = OrderedDict([(request_def, request_schema), (response_def, response_schema)])
    swagger["x-temu-source"] = operation.get("source")
    swagger["x-temu-api-type"] = api_type
    swagger["x-temu-region-module"] = operation.get("regionModule")
    return swagger


def slugify(value: str) -> str:
    value = re.sub(r"^\d+\s*[、.．]\s*", "", value or "").strip().lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "misc"


def group_slug(region_key: str, group_title: str, api_type: str = "") -> tuple[str, str]:
    if region_key == "temu-cn-api":
        if group_title in CN_GROUP_MAP:
            return CN_GROUP_MAP[group_title]
        if api_type.startswith("bg.marketing."):
            return CN_GROUP_MAP["活动API组-PA"]
        if api_type.startswith("bg.semi.") or api_type.startswith("bg.price.") or "price" in api_type:
            return CN_GROUP_MAP["申报价/核价/调价API-PA"]
        return slugify(group_title) + "-api", group_title or "Misc"
    normalized = re.sub(r"^\d+\s*[、.．]\s*", "", group_title or "").strip().replace("Rufund", "Refund")
    low = normalized.lower().strip()
    if low in REGION_GROUP_MAP:
        return REGION_GROUP_MAP[low]
    for key, result in REGION_GROUP_MAP.items():
        if key in low:
            return result
    if not normalized and api_type.startswith("temu.logistics."):
        return REGION_GROUP_MAP["logistics"]
    return slugify(normalized) + "-api", normalized or "Misc"


def split_table_row(line: str) -> list[str]:
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [clean_cell(cell) for cell in raw.split("|")]


def is_alignment_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.match(r"^:?-{3,}:?$", cell.replace(" ", "")) for cell in cells)


def parse_table_rows(table_lines: list[str]) -> tuple[list[str], list[OrderedDict]]:
    rows = [split_table_row(line) for line in table_lines]
    rows = [row for row in rows if any(cell for cell in row)]
    if len(rows) >= 2 and is_alignment_row(rows[1]):
        headers, data = rows[0], rows[2:]
    else:
        headers, data = (rows[0], rows[1:]) if rows else ([], [])
    parsed = []
    for row in data:
        row = row + [""] * max(0, len(headers) - len(row))
        item = OrderedDict((header or f"col{i + 1}", row[i] if i < len(row) else "") for i, header in enumerate(headers))
        if any(str(value).strip() for value in item.values()):
            parsed.append(item)
    return headers, parsed


def previous_label(lines: list[str], idx: int) -> str:
    pos = idx - 1
    while pos >= 0:
        text = clean_cell(lines[pos])
        if text and text not in STOP_LABELS and not text.startswith("```"):
            return text
        pos -= 1
    return ""


def required_value(raw):
    value = str(raw).strip().lower()
    if value in {"是", "true", "yes", "required"}:
        return True
    if value in {"否", "false", "no", "optional"}:
        return False
    return raw


def normalize_param_row(row: OrderedDict) -> OrderedDict:
    def pick(*names: str) -> str:
        for name in names:
            for key, value in row.items():
                if key.lower() == name.lower():
                    return value
        return ""

    param = OrderedDict()
    param["name"] = pick("参数接口", "Properties", "Property", "Parameter", "参数", "字段", "name")
    typ = pick("参数类型", "Type", "类型")
    req = pick("是否必填", "Required", "是否必须", "必填")
    desc = pick("说明", "Description", "描述")
    if typ:
        param["type"] = typ
    if req != "":
        param["required"] = required_value(req)
    if desc:
        param["description"] = desc
    return param


def add_dictionary_reference(param: OrderedDict, is_request: bool = True) -> None:
    name = str(param.get("name", "")).strip()
    desc = str(param.get("description", "")).strip()
    target = reason = None
    if name in DICT_ANCHORS:
        target, reason = DICT_ANCHORS[name]
    elif is_request:
        for pattern, pair in DICT_DESC_PATTERNS:
            if pattern.search(name) or pattern.search(desc):
                target, reason = pair
                break
    if not target:
        return
    param["offlineReference"] = f"../../offline-docs/data-dictionary.md#{target}"
    param["offlineReferenceReason"] = reason
    if "http" in desc and ("894069632221" in desc or "partner.kuajingmaihuo.com/document" in desc):
        param["description"] = re.sub(r"https?://\S+", f"../../offline-docs/data-dictionary.md#{target}", desc)


def parse_operation_block(
    lines: list[str],
    start_idx: int,
    end_idx: int,
    heading_line: int,
    api_type: str,
    group_title: str | None,
    region_key: str,
    source_path: Path,
) -> OrderedDict:
    block = lines[start_idx + 1 : end_idx]
    block_text = "\n".join(block).strip("\n")
    nonempty = [clean_cell(line) for line in block if clean_cell(line)]

    last_update = None
    description = ""
    audience = []
    for text in nonempty[:24]:
        update = re.search(r"更新时间[:：]\s*(.+)", text) or re.search(r"Last update time:\s*(.+)", text, flags=re.I)
        if update:
            last_update = update.group(1).strip()
        if text.startswith("接口介绍"):
            description = re.sub(r"^接口介绍[:：]\s*", "", text).strip()
        elif text.startswith("Description:"):
            description = text.split(":", 1)[1].strip()
        tag_part = re.sub(r"Last update time:.*$", "", text).strip()
        if tag_part in {"Local", "Cross Border", "LocalCross Border"}:
            if "Local" in tag_part:
                audience.append("Local")
            if "Cross" in tag_part:
                audience.append("Cross Border")

    summary = ""
    noise = {
        "收起",
        "Show Less",
        "Show More",
        "公共参数",
        "Common Parameters",
        "Request URL",
        "请求地址",
        "公共请求参数",
        "请求参数说明",
        "Request",
        "Response",
        "返回参数说明",
        "Rate Limiting Rules",
    }
    for text in nonempty[:16]:
        if text in noise:
            continue
        if text.startswith(("更新时间", "接口介绍", "Description:", "Last update time")) or "Last update time:" in text:
            continue
        if text.startswith("|") or text.startswith("Rate Limiting"):
            continue
        summary = text
        break
    if not summary:
        summary = description or api_type
    if not description:
        description = summary

    tables = []
    index = 0
    while index < len(block):
        if block[index].lstrip().startswith("|"):
            table_start = index
            table_lines = []
            while index < len(block) and block[index].lstrip().startswith("|"):
                table_lines.append(block[index])
                index += 1
            headers, rows = parse_table_rows(table_lines)
            tables.append({"label": previous_label(block, table_start), "headers": headers, "rows": rows})
        else:
            index += 1

    endpoints = []
    common_parameters = []
    request_parameters = []
    response_parameters = []
    rate_limits = []
    additional_tables = []
    for table in tables:
        label = table["label"]
        headers_text = " ".join(table["headers"]).lower()
        if "request url" in headers_text or "调用地址" in headers_text or "请求地址" in label:
            endpoints.extend(table["rows"])
        elif label == "公共请求参数" or (label == "Common Parameters" and ("properties" in headers_text or "参数接口" in headers_text)):
            common_parameters.extend(normalize_param_row(row) for row in table["rows"])
        elif label in {"请求参数说明", "Request"}:
            request_parameters.extend(normalize_param_row(row) for row in table["rows"])
        elif label in {"返回参数说明", "Response"}:
            response_parameters.extend(normalize_param_row(row) for row in table["rows"])
        elif "rate limiting" in label.lower() or "限流" in label:
            rate_limits.extend(table["rows"])
        else:
            additional_tables.append({"label": label, "rows": table["rows"]})

    if not common_parameters:
        common_parameters = copy.deepcopy(COMMON_REQUEST_PARAMS)
    if region_key == "temu-cn-api":
        for param in request_parameters:
            add_dictionary_reference(param, is_request=True)

    examples = []
    for match in re.finditer(r"```([^\n`]*)\n(.*?)```", block_text, flags=re.S):
        body = match.group(2).strip("\n")
        if not body.strip():
            continue
        truncated = False
        if len(body) > 12000:
            body = body[:12000].rstrip() + "\n... [truncated]"
            truncated = True
        examples.append({"language": match.group(1).strip() or "text", "content": body, "truncated": truncated})
        if len(examples) >= 4:
            break

    gslug, gtitle = group_slug(region_key, group_title or "", api_type)
    gateway_url = REGION_META[region_key]["defaultGateway"]
    if endpoints:
        source_endpoint_text = json.dumps(endpoints, ensure_ascii=False)
        explicit = re.search(r"https?://[^\s|]+/openapi/router", source_endpoint_text)
        if explicit:
            gateway_url = explicit.group(0)
        elif "/openapi/router" in source_endpoint_text:
            gateway_url = "/openapi/router"
    if region_key == "temu-cn-api" and ((group_title and "PA" in group_title) or api_type.startswith(("bg.glo.", "bg.btg.")) or api_type.endswith(".global")):
        gateway_url = "https://openapi-b-partner.temu.com/openapi/router"

    operation = OrderedDict()
    operation["apiType"] = api_type
    operation["operationId"] = api_type.replace(".", "_")
    operation["title"] = summary
    operation["description"] = description
    operation["regionModule"] = region_key
    operation["group"] = {"title": gtitle, "sourceTitle": group_title or "", "directory": gslug}
    operation["gateway"] = {"method": "POST", "url": gateway_url, "routerTypeParameter": "type"}
    if gateway_url == "/openapi/router" and REGION_META[region_key].get("defaultGatewayNote"):
        operation["gateway"]["note"] = REGION_META[region_key]["defaultGatewayNote"]
    if endpoints:
        operation["endpointTable"] = endpoints
    if audience:
        operation["audience"] = sorted(set(audience))
    if last_update:
        operation["lastUpdateTime"] = last_update
    operation["commonParameters"] = common_parameters
    operation["requestParameters"] = request_parameters
    operation["responseParameters"] = response_parameters
    if rate_limits:
        operation["rateLimiting"] = rate_limits
    if examples:
        operation["examples"] = examples
    if additional_tables:
        operation["additionalTables"] = additional_tables[:8]
    operation["source"] = {
        "document": source_path.name,
        "path": str(source_path),
        "startLine": heading_line,
        "endLine": heading_line + max(0, end_idx - start_idx - 1),
        "contentSha256": hashlib.sha256(block_text.encode("utf-8")).hexdigest(),
    }
    return operation


def extract_operations(region_key: str, source_key: str, group_override: str | None = None) -> list[OrderedDict]:
    source_path = SOURCES[source_key]
    lines = read_text(source_path).splitlines()
    headings = []
    current_h1 = None
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        if level == 1:
            current_h1 = title
        if level == 2 and API_RE.match(title):
            headings.append({"idx": idx, "line": idx + 1, "apiType": title, "group": group_override if group_override is not None else current_h1})
    operations = []
    for pos, heading in enumerate(headings):
        end_idx = headings[pos + 1]["idx"] if pos + 1 < len(headings) else len(lines)
        operations.append(parse_operation_block(lines, heading["idx"], end_idx, heading["line"], heading["apiType"], heading["group"], region_key, source_path))
    return operations


def parse_cn_migrations() -> list[dict]:
    text = read_text(SOURCES["cn"])
    start = text.find("## 二、已迁移")
    end = text.find("## 三、FAQ")
    if start < 0 or end < 0:
        return []
    migrations = []
    current_period = None
    for line in text[start:end].splitlines():
        heading = re.match(r"###\s+(.+)", line)
        if heading:
            current_period = heading.group(1).strip()
            continue
        if not line.startswith("|") or "---" in line or "接口组" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if api_tokens(cells[3]):
            desc, new, old = clean_cell(cells[1]) or clean_cell(cells[0]), api_tokens(cells[2]), api_tokens(cells[3])
        elif api_tokens(cells[2]) and api_tokens(cells[1]):
            desc, new, old = clean_cell(cells[0]), api_tokens(cells[1]), api_tokens(cells[2])
        else:
            desc, new, old = clean_cell(cells[1]) or clean_cell(cells[0]), api_tokens(cells[2]), api_tokens(cells[3])
        if new and old:
            migrations.append(
                {
                    "period": current_period,
                    "description": desc,
                    "newTypes": new,
                    "legacyTypes": old,
                    "legacyStillActiveForFullManaged": "全托仍使用原接口" in "".join(cells),
                    "sourceRow": clean_cell(line),
                }
            )
    return migrations


def select_primary_new(new_types: list[str], existing_types) -> str:
    for api_type in new_types:
        if api_type in existing_types and api_type.startswith("bg."):
            return api_type
    for api_type in new_types:
        if api_type in existing_types:
            return api_type
    for api_type in new_types:
        if api_type.startswith("bg."):
            return api_type
    return new_types[0]


def infer_cn_pa_group(api_type: str, legacy_group: str) -> str:
    if api_type.startswith("bg.marketing."):
        return "活动API组-PA"
    if api_type.startswith("bg.semi.") or "price" in api_type:
        return "申报价/核价/调价API-PA"
    if legacy_group and legacy_group + "-PA" in CN_GROUP_MAP:
        return legacy_group + "-PA"
    return legacy_group or "PA网关调用说明"


def prefer_operation(existing: OrderedDict, candidate: OrderedDict) -> OrderedDict:
    api_type = existing["apiType"]
    old_group = existing["group"]["sourceTitle"]
    new_group = candidate["group"]["sourceTitle"]
    if "virtualinventoryjit" in api_type and "JIT" in new_group and "JIT" not in old_group:
        return candidate
    if "warehouse.list.get" in api_type and "库存" in new_group and "库存" not in old_group:
        return candidate
    return existing


def dedupe_operations(operations: list[OrderedDict]) -> list[OrderedDict]:
    by_type = OrderedDict()
    duplicates = defaultdict(list)
    for operation in operations:
        api_type = operation["apiType"]
        if api_type not in by_type:
            by_type[api_type] = operation
            continue
        duplicates[api_type].append(operation["source"])
        chosen = prefer_operation(by_type[api_type], operation)
        if chosen is operation:
            duplicates[api_type].append(by_type[api_type]["source"])
            by_type[api_type] = operation
    for api_type, sources in duplicates.items():
        by_type[api_type]["deduplicatedSources"] = sources
    return list(by_type.values())


def apply_cn_migrations(operations: list[OrderedDict]) -> tuple[list[OrderedDict], list[dict], list[str], list[str]]:
    by_type = OrderedDict((operation["apiType"], operation) for operation in dedupe_operations(operations))
    excluded = set()
    synthesized = []
    migrations = parse_cn_migrations()
    for migration in migrations:
        primary = select_primary_new(migration["newTypes"], by_type.keys())
        aliases = [api_type for api_type in migration["newTypes"] if api_type != primary]
        for legacy in migration["legacyTypes"]:
            if primary not in by_type and legacy in by_type:
                replacement = copy.deepcopy(by_type[legacy])
                replacement["apiType"] = primary
                replacement["operationId"] = primary.replace(".", "_")
                replacement["gateway"] = {"method": "POST", "url": "https://openapi-b-partner.temu.com/openapi/router", "routerTypeParameter": "type"}
                source_group = infer_cn_pa_group(primary, by_type[legacy]["group"]["sourceTitle"])
                gslug, gtitle = group_slug("temu-cn-api", source_group, primary)
                replacement["group"] = {"title": gtitle, "sourceTitle": source_group, "directory": gslug}
                replacement["description"] = (replacement.get("description") or migration["description"]) + " PA gateway replacement generated from the legacy schema because the source migration table lists the new type but the detailed PA section is not present."
                replacement["schemaCopiedFromLegacyType"] = legacy
                replacement["source"]["generatedFromMigrationRow"] = migration["sourceRow"]
                replacement["synthetic"] = True
                by_type[primary] = replacement
                synthesized.append(primary)
            if primary in by_type:
                operation = by_type[primary]
                meta = operation.setdefault("migration", OrderedDict())
                replaces = meta.setdefault("replacesLegacyTypes", [])
                if legacy not in replaces:
                    replaces.append(legacy)
                if aliases:
                    alt = operation.setdefault("alternateApiTypes", [])
                    for alias in aliases:
                        if alias not in alt:
                            alt.append(alias)
                meta["period"] = migration["period"]
                meta["description"] = migration["description"]
                meta["partnerGatewayUrl"] = "https://openapi-b-partner.temu.com/openapi/router"
                if migration["legacyStillActiveForFullManaged"]:
                    meta["legacyStillActiveForFullManaged"] = True
            if legacy in by_type:
                if migration["legacyStillActiveForFullManaged"]:
                    legacy_op = by_type[legacy]
                    legacy_op.setdefault("migration", OrderedDict())["note"] = "Source migration table says this legacy type is still used for full-managed flows; use the PA replacement for semi-managed flows."
                    legacy_op["migration"]["semiManagedReplacementTypes"] = migration["newTypes"]
                else:
                    excluded.add(legacy)
    return [operation for api_type, operation in by_type.items() if api_type not in excluded], migrations, sorted(excluded), sorted(set(synthesized))


def normalize_dictionary(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)\n?", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    replacements = {
        "***\\*siteId\\****": "siteId",
        "***\\*siteName\\****": "siteName",
        "***\\*是否开站\\****": "是否开站",
        "***\\*关联站点\\****": "关联站点",
        "***\\*catId\\****": "catId",
        "***\\*catName\\****": "catName",
        "***\\*limit\\****": "limit",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if len(line) > 240 and re.fullmatch(r"[\d,\s]+", line):
            values = [item for item in re.split(r"\s*,\s*", line.strip()) if item]
            for start in range(0, len(values), 24):
                lines.append(", ".join(values[start : start + 24]))
        else:
            lines.append(line)
    compact = []
    blank = False
    for line in lines:
        if not line:
            if not blank:
                compact.append("")
            blank = True
        else:
            compact.append(line)
            blank = False
    intro = """# Temu CN Offline Data Dictionary

This file is a cleaned local copy of `Temu CN 数据字典(1).md` for offline agents. Use it when CN operation fields mention site IDs, province IDs, size-chart classes, product-name limits, shipping promises, model requirements, or other fixed Temu reference values.

## Quick Index

| Topic | Common fields |
| --- | --- |
| [半托管发品sku分类必传的叶子类目](#半托管发品sku分类必传的叶子类目) | `skuClassification` |
| [尺码表分类](#尺码表分类) | `classId`, `className` |
| [发品-省份枚举值](#发品-省份枚举值) | `productWhExtAttrReq.productOrigin.region2Id`, `provinceCode` |
| [定制品定制工艺层级关系](#定制品定制工艺层级关系) | `firstType`, `twiceType` |
| [半托管站点列表](#半托管站点列表) | `siteId`, `siteIdList`, `bindSiteIds`, `semiManagedSiteMode` |
| [货品名称长度限制规则](#货品名称长度限制规则) | `productName` |
| [净含量必填叶子类目](#净含量必填叶子类目) | net-content fields |
| [承诺发货时效说明](#承诺发货时效说明) | `shipmentLimitSecond` |
| [车型库必填类目](#车型库必填类目) | vehicle library required categories |
| [支持底板套板的类目](#支持底板套板的类目) | `isBasePlate` and base-plate category checks |

Notes:

- Long category ID lists are intentionally preserved because they are value references, not prose.
- Duplicate blank lines and exported image links were removed.
- For dynamic values that depend on seller/category state, prefer the relevant Temu API first, then use this file as the static offline fallback.

"""
    footer = f"""

## Source Checked

- Local source: `{SOURCES["cn_dict"]}`
- Generated from the downloaded Markdown file. No online page was fetched during this build.
"""
    return intro + "\n".join(compact).strip() + "\n" + footer


def generate_group_readme(group_dir: Path, group_title: str, source_title: str, operations: list[OrderedDict]) -> None:
    lines = [f"# {group_title} API", "", f"Source group: `{source_title or group_title}`.", "", "## API List", ""]
    for operation in sorted(operations, key=lambda item: item["apiType"]):
        desc = (operation.get("description") or operation.get("title") or "").replace("\n", " ").strip()
        if len(desc) > 180:
            desc = desc[:177] + "..."
        lines.append(f"- [{operation['apiType']}](operations/{operation_filename(operation['apiType'])}) - {desc}")
    lines.append("")
    write_text(group_dir / "README.md", "\n".join(lines))


def generate_region_readme(region_key: str, operations: list[OrderedDict], extra: list[str] | None = None) -> None:
    meta = REGION_META[region_key]
    groups = defaultdict(list)
    for operation in operations:
        groups[operation["group"]["directory"]].append(operation)
    lines = [
        f"# {meta['title']}",
        "",
        meta["description"],
        "",
        "## How To Call",
        "",
        "All operation files are Swagger 2.0 documents. Temu router APIs are called with `POST` and a `type` parameter. Put common auth/signature fields together with the operation request fields in the JSON body unless your runtime wraps common parameters separately.",
        "",
        f"Default gateway: `{meta['defaultGateway']}`",
    ]
    if meta.get("defaultGatewayNote"):
        lines.extend(["", f"Note: {meta['defaultGatewayNote']}"])
    if region_key == "temu-cn-api":
        lines.extend(["", "For fields whose values come from the CN data dictionary, use [offline-docs/data-dictionary.md](offline-docs/data-dictionary.md)."])
    lines.extend(["", "## API Groups", ""])
    for slug in sorted(groups):
        gops = groups[slug]
        lines.append(f"- [{gops[0]['group']['title']}](./{slug}/README.md) - {len(gops)} operations")
    if extra:
        lines.extend(["", "## Build Notes", ""])
        lines.extend(f"- {item}" for item in extra)
    lines.extend(["", "## Source Checked", "", f"- `{SOURCES[meta['sourceKey']]}`"])
    if region_key == "temu-eu-api":
        lines.append(f"- `{SOURCES['eu_add']}`")
    lines.append("")
    write_text(OUT / region_key / "README.md", "\n".join(lines))


def build_index(all_region_ops: OrderedDict[str, list[OrderedDict]], stats: OrderedDict) -> OrderedDict:
    index = OrderedDict()
    index["generatedAt"] = datetime.now().isoformat(timespec="seconds")
    index["sourceDocuments"] = {key: str(path) for key, path in SOURCES.items()}
    index["stats"] = stats
    for region_key, operations in all_region_ops.items():
        groups = defaultdict(list)
        for operation in operations:
            groups[operation["group"]["directory"]].append(
                {
                    "apiType": operation["apiType"],
                    "title": operation.get("title", ""),
                    "description": operation.get("description", ""),
                    "path": f"{operation['group']['directory']}/operations/{operation_filename(operation['apiType'])}",
                    "gateway": operation.get("gateway", {}).get("url"),
                }
            )
        index[region_key] = {"groups": OrderedDict((key, sorted(value, key=lambda item: item["apiType"])) for key, value in sorted(groups.items()))}
    return index


def generate_root_readme(index: OrderedDict) -> None:
    lines = [
        "# Temu API Models",
        "",
        "AI-friendly local Temu API documentation generated from the downloaded Markdown source files. The structure mirrors the local Amazon API docs style: regional API modules, API group READMEs, and operation-level Swagger 2.0 JSON files under `operations/`.",
        "",
        "## Routing Rules",
        "",
        "- Chinese cross-border stores, including full-managed and semi-managed stores, use [temu-cn-api](./temu-cn-api/README.md) for inventory.",
        "- Chinese cross-border semi-managed stores should use the destination-region API for order-related operations.",
        "- European local stores use [temu-eu-api](./temu-eu-api/README.md).",
        "- US local stores use [temu-us-api](./temu-us-api/README.md).",
        "- Americas outside the US use [temu-global-api](./temu-global-api/README.md).",
        "",
        "## Calling Model",
        "",
        "Temu router APIs are generally `POST` requests to an `/openapi/router` endpoint. Each operation JSON is a standalone Swagger 2.0 file with one `POST /openapi/router` operation. The API operation is selected by the `type` field, and common fields such as `app_key`, `access_token`, `timestamp`, `sign`, `data_type`, and `version` appear in the request body schema.",
        "",
        "For CN APIs, some legacy CN gateway `type` values have migrated to the PA gateway. This local model prefers the PA replacement type when the source migration table marks the old type as migrated; old types that the source explicitly says are still used for full-managed flows are retained with migration notes.",
        "",
        "## Modules",
        "",
    ]
    for region_key in ["temu-cn-api", "temu-us-api", "temu-eu-api", "temu-global-api"]:
        count = sum(len(value) for value in index[region_key]["groups"].values())
        lines.append(f"- [{REGION_META[region_key]['title']}](./{region_key}/README.md) - {count} operations")
    lines.extend(
        [
            "",
            "## Offline References",
            "",
            "- [Temu CN data dictionary](./temu-cn-api/offline-docs/data-dictionary.md) - local reference values used by CN product/inventory fields.",
            "",
            "## Source Checked",
            "",
        ]
    )
    for key in ["cn_dict", "cn", "us", "eu", "eu_add", "global"]:
        lines.append(f"- `{SOURCES[key]}`")
    lines.append("")
    write_text(OUT / "README.md", "\n".join(lines))


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    all_region_ops = OrderedDict()
    stats = OrderedDict()

    cn_raw = extract_operations("temu-cn-api", "cn")
    cn_ops, migrations, excluded, synthesized = apply_cn_migrations(cn_raw)
    all_region_ops["temu-cn-api"] = sorted(cn_ops, key=lambda item: (item["group"]["directory"], item["apiType"]))
    stats["temu-cn-api"] = {
        "rawOperations": len(cn_raw),
        "activeOperations": len(cn_ops),
        "migrationRows": len(migrations),
        "excludedLegacyTypes": excluded,
        "synthesizedPartnerOperations": synthesized,
    }

    us_ops = dedupe_operations(extract_operations("temu-us-api", "us"))
    all_region_ops["temu-us-api"] = sorted(us_ops, key=lambda item: (item["group"]["directory"], item["apiType"]))
    stats["temu-us-api"] = {"rawOperations": len(us_ops), "activeOperations": len(us_ops)}

    eu_ops = dedupe_operations(extract_operations("temu-eu-api", "eu") + extract_operations("temu-eu-api", "eu_add", group_override="Logistics"))
    all_region_ops["temu-eu-api"] = sorted(eu_ops, key=lambda item: (item["group"]["directory"], item["apiType"]))
    stats["temu-eu-api"] = {"rawOperationsIncluding0416": len(eu_ops), "activeOperations": len(eu_ops)}

    global_ops = dedupe_operations(extract_operations("temu-global-api", "global"))
    all_region_ops["temu-global-api"] = sorted(global_ops, key=lambda item: (item["group"]["directory"], item["apiType"]))
    stats["temu-global-api"] = {"rawOperations": len(global_ops), "activeOperations": len(global_ops)}

    for region_key, operations in all_region_ops.items():
        grouped = defaultdict(list)
        for operation in operations:
            group_dir = OUT / region_key / operation["group"]["directory"]
            write_json(group_dir / "operations" / operation_filename(operation["apiType"]), operation_to_swagger(operation))
            grouped[operation["group"]["directory"]].append(operation)
        for slug, group_ops in grouped.items():
            generate_group_readme(OUT / region_key / slug, group_ops[0]["group"]["title"], group_ops[0]["group"]["sourceTitle"], group_ops)

    write_text(OUT / "temu-cn-api" / "offline-docs" / "data-dictionary.md", normalize_dictionary(read_text(SOURCES["cn_dict"])))

    cn_notes = [
        f"Excluded {len(excluded)} migrated legacy CN types when a PA replacement was available or synthesized.",
        f"Synthesized {len(synthesized)} PA operation files from legacy schemas because the migration table listed a PA type without a detailed PA section.",
    ]
    for region_key, operations in all_region_ops.items():
        generate_region_readme(region_key, operations, cn_notes if region_key == "temu-cn-api" else None)

    index = build_index(all_region_ops, stats)
    generate_root_readme(index)

    print(
        json.dumps(
            {
                "out": str(OUT),
                "stats": stats,
                "totalFiles": sum(1 for path in OUT.rglob("*") if path.is_file()),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
