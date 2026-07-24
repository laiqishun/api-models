# API Models

This repository collects API model documentation in an AI-friendly, progressively disclosed format. It is designed so a reader or coding agent can start from a small index, choose the API family it needs, then drill down to module or group READMEs and final operation-level Swagger/OpenAPI JSON files.

The current dataset contains:

- [Amazon Selling Partner API Models](amazon-sp-api/README.md)
- [Amazon Ads API Models](amazon-ads-api/README.md)
- [Temu API Models](temu-api/README.md)

## Structure

Each top-level directory represents one API family or platform:

```text
api-models/
  amazon-sp-api/
  amazon-ads-api/
  temu-api/
```

Inside an API family, the expected navigation pattern is:

```text
README.md
  -> API family README.md
     -> module or group README.md
        -> operation-level Swagger/OpenAPI JSON
```

This keeps broad discovery lightweight while still preserving the detailed endpoint schemas needed for implementation, validation, code generation, and AI-assisted development.

## Current Scope

`amazon-sp-api` contains processed Amazon Selling Partner API model documentation. Each module README summarizes the API area and links to focused operation files under `operations/`. Those operation JSON files are self-contained around a single endpoint and include the schemas needed by that endpoint.

`amazon-ads-api` contains processed Amazon Ads API model documentation. Its group READMEs are organized from the source OpenAPI operation tags and link to focused operation files under `operations/`.

`temu-api` contains processed Temu CN, US local, EU local, and global local API documentation. It follows the same progressive disclosure pattern, with regional routing guidance, group READMEs, operation-level Swagger 2.0 JSON files, and a CN offline data dictionary for reference values that otherwise live in source docs.

## Future Scope

Additional API families can be added as sibling directories when they are processed into the same format. For example:

- `tiktok-sp-api` for TikTok APIs

New API families should provide their own top-level README and follow the same progressive disclosure pattern so the root index remains stable and easy to scan.
