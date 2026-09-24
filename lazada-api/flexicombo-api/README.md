---
title: "Lazada Flexicombo API"
description: "The APIs for Flexicombo Tools"
---

# API List

- [ActivateFlexiCombo](operations/activate-flexi-combo.json) (POST /promotion/flexicombo/activate) — activate flexi combo
- [AddFlexiComboProducts](operations/add-flexi-combo-products.json) (POST /promotion/flexicombo/products/add) — add flexi combo products
- [CreateFlexiCombo](operations/create-flexi-combo.json) (POST /promotion/flexicombo/create) — create a  new promotion flexi combo
- [DeactivateFlexiCombo](operations/deactivate-flexi-combo.json) (POST /promotion/flexicombo/deactivate) — deactivate flexi combo
- [DeleteFlexiComboProducts](operations/delete-flexi-combo-products.json) (POST /promotion/flexicombo/products/delete) — delete flexi combo products
- [GetFlexiComboDetails](operations/get-flexi-combo-details.json) (GET /promotion/flexicombo/details) — get promotion flexi combo detail by id
- [ListFlexiCombo](operations/list-flexi-combo.json) (GET /promotion/flexicombo/list) — list flexi combo
- [ListFlexiComboProducts](operations/list-flexi-combo-products.json) (GET /promotion/flexicombo/products/list) — list flexi combo products
- [UpdateFlexiCombo](operations/update-flexi-combo.json) (POST /promotion/flexicombo/update) — update flexi combo

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
