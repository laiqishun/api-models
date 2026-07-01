# API Models

This repository collects API model documentation in an AI-friendly, progressively disclosed format. It is designed so a reader or coding agent can start from a small index, choose the API family it needs, then drill down to module READMEs and final operation-level Swagger JSON files.

The current dataset contains Amazon Selling Partner API models:

- [Amazon Selling Partner API Models](amazon-sp-api-models/README.md)

## Structure

Each top-level directory represents one API family or platform:

```text
api-models/
  amazon-sp-api-models/
  amazon-ads-sp-api-models/
  tiktok-sp-api-models/
```

Inside an API family, the expected navigation pattern is:

```text
README.md
  -> module README.md
     -> operation-level Swagger JSON
```

This keeps broad discovery lightweight while still preserving the detailed endpoint schemas needed for implementation, validation, code generation, and AI-assisted development.

## Current Scope

`amazon-sp-api-models` contains processed Amazon Selling Partner API model documentation. Each module README summarizes the API area and links to focused operation files under `operations/`. Those operation JSON files are self-contained around a single endpoint and include the schemas needed by that endpoint.

## Future Scope

Additional API families can be added as sibling directories when they are processed into the same format. For example:

- `amazon-ads-sp-api-models` for Amazon Ads APIs
- `tiktok-sp-api-models` for TikTok APIs

New API families should provide their own top-level README and follow the same progressive disclosure pattern so the root index remains stable and easy to scan.
