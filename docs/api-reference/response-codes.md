# Response Codes

| Code | Status | Description |
|------|--------|-------------|
| 200 | OK | The request has succeeded. |
| 307 | Temporary Redirect | The requested resource is temporarily available at a different URL. |
| 400 | Bad Request | Arguments are not correctly transmitted. |
| 401 | Unauthorized | You forgot to add the token to the query. |
| 402 | Payment Required | Payment is required to access HikerAPI. |
| 403 | Forbidden | The account, comment, or media is private. |
| 404 | Not Found | The account, comment, or media was not found. |
| 405 | Method Not Allowed | This HTTP method is not allowed for HikerAPI. |
| 408 | Request Timeout | The server waited too long and closed the connection. |
| 410 | Gone | The endpoint is deprecated and retired (request fee is **not** charged). Use the alternative from the endpoint's docs. |
| 422 | Unprocessable Entity | The server understands the request but cannot process it due to semantic errors. |
| 429 | Too Many Requests | Your request was rejected due to exceeding the request limit. See [Rate Limits](../guides/rate-limits.md). |
| 430 | Request Header Fields Too Large | Request header fields too large. |
| 500 | Internal Server Error | Internal server error (request fee is **not** charged). |
| 503 | Service Unavailable | Server temporarily unable to process requests (request fee is **not** charged). |
| 504 | Gateway Timeout | Network delays or server access problems (request fee is **not** charged). |

!!! info "Billing note"
    Only `200`, `400`, `403` and `404` responses are charged — the API does the work even when the result is "not found" or "private". Everything else is free: deprecated endpoints respond with `410 Gone` and are never charged, and `50x` server errors are not charged either.
