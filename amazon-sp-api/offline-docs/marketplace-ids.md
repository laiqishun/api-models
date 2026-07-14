# Marketplace IDs / Store Identifiers

Use a `marketplaceId` value to tell SP-API which Amazon store a request targets. Many operations accept `marketplaceIds` as an array.

Choose the store first, then pass the exact `marketplaceId` string. For regional SP-API host selection, use the region group shown below.

## North America and Brazil

Use the NA SP-API endpoint for these stores: `sellingpartnerapi-na.amazon.com`.

| Country | Country code | marketplaceId |
| --- | --- | --- |
| Canada | CA | `A2EUQ1WTGCTBG2` |
| United States of America | US | `ATVPDKIKX0DER` |
| Mexico | MX | `A1AM78C64UM0Y8` |
| Brazil | BR | `A2Q3Y263D00KWC` |

## Europe, Middle East, India, and Africa

Use the EU SP-API endpoint for these stores: `sellingpartnerapi-eu.amazon.com`.

| Country | Country code | marketplaceId |
| --- | --- | --- |
| Ireland | IE | `A28R8C7NBKEWEA` |
| Spain | ES | `A1RKKUPIHCS9HS` |
| United Kingdom | UK | `A1F83G8C2ARO7P` |
| France | FR | `A13V1IB3VIYZZH` |
| Belgium | BE | `AMEN7PMS3EDWL` |
| Netherlands | NL | `A1805IZSGTT6HS` |
| Germany | DE | `A1PA6795UKMFR9` |
| Italy | IT | `APJ6JRA9NG5V4` |
| Sweden | SE | `A2NODRKZP88ZB9` |
| South Africa | ZA | `AE08WJ6YKNBMC` |
| Poland | PL | `A1C3SOZRARQ6R3` |
| Egypt | EG | `ARBP9OOSHTCHU` |
| Turkey | TR | `A33AVAJ2PDY3EV` |
| Saudi Arabia | SA | `A17E79C6D8DWNP` |
| United Arab Emirates | AE | `A2VIGQ35RCS4UG` |
| India | IN | `A21TJRUUN4KGV` |

## Far East

Use the FE SP-API endpoint for these stores: `sellingpartnerapi-fe.amazon.com`.

| Country | Country code | marketplaceId |
| --- | --- | --- |
| Singapore | SG | `A19VAU5U5O7RUS` |
| Australia | AU | `A39IBJ37TRP1C6` |
| Japan | JP | `A1VC38T7YXB528` |

## Filling parameters

- `marketplaceId`: pass one exact string, for example `ATVPDKIKX0DER`.
- `marketplaceIds`: pass an array of exact strings, for example `["ATVPDKIKX0DER"]`.
- Do not pass country codes such as `US` or display names such as `United States`.
- Some operations support only a subset of stores. If the operation description names supported countries, use that subset even if the store appears in this file.

Source checked: Amazon SP-API Store Identifiers / Marketplace IDs online documentation, 2026-07-14.

Online source URLs:

- https://developer-docs.amazon/sp-api/docs/marketplace-ids
