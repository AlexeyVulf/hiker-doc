# Request Costs

Each API call may use one or more internal request units. The actual cost is returned in the response header:

```
x-hiker-info: {"reqs": 1}
```

Most endpoints cost **1 request**. Some endpoints perform additional checks (privacy, ID lookup) and cost more.

Retired endpoints respond with [`410 Gone`](../api-reference/response-codes.md) and `reqs=0` — such calls are never charged.

## Multi-request endpoints

| Endpoint | Reqs | What it does |
|----------|------|-------------|
| `/v1/user/highlights` | 2 | Gets highlights + privacy check |
| `/v2/user/highlights` | 2 | Gets highlights + privacy check |
| `/v1/user/highlights/by/username` | 3 | Username→ID lookup + highlights + privacy check |
| `/v2/user/highlights/by/username` | 3 | Username→ID lookup + highlights + privacy check |
| `/v1/user/stories` | 2 | Gets stories + privacy check |
| `/v2/user/stories` | 2 | Gets stories + privacy check |
| `/v1/user/stories/by/username` | 3 | Username→ID lookup + stories + privacy check |
| `/v2/user/stories/by/username` | 3 | Username→ID lookup + stories + privacy check |
| `/v1/user/search/followers` | 2 | Gets followers + privacy check |
| `/v1/user/search/following` | 2 | Gets following + privacy check |
| `/a2/user` | 2 | Profile data + media |
| `/v2/user/explore/businesses/by/id` | 2 | Business recommendations + account details |
| `/gql/user/followers/chunk` | 2 | Gets followers + privacy check |
| `/gql/user/following/chunk` | 2 | Gets following + privacy check |

## Force mode — skip privacy checks

Add `force=on` to skip privacy checks and reduce request cost by 1:

=== "With force (1 req)"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories?user_id=123&force=on"
    ```

=== "Without force (2 reqs)"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories?user_id=123"
    ```

!!! note
    Privacy checks identify **private accounts** specifically. Shadow-banned, deleted, or suspended accounts are handled differently.
