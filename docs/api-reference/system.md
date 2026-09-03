# System Endpoints

Account balance and rate limit info.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../getting-started/authentication.md). Error responses: [Response Codes](response-codes.md).

**Endpoints:** [`/sys/balance`](#get-sysbalance)

---

### GET /sys/balance

Balance of your account: how many requests are left and how much money is on it.

**The two values refresh at different rates:**

* `requests` is **real time** — it goes down with every call you make.
* `amount` is **settled once per hour** — spending is charged in whole
  hours, a few minutes after the hour ends. Between charges `amount` looks
  frozen even though you are spending. Top-ups are the exception: they
  appear within seconds.

So use `requests` for quota checks and low-balance alerts, and `amount` for
accounting. Calling this endpoint is free — it does not consume a request.

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/sys/balance"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/sys/balance",
        headers={"x-access-key": "YOUR_TOKEN"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/sys/balance",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "requests": 1992006,
  "rate": 15,
  "currency": "USD",
  "amount": 916.3235
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-system){ target=_blank }
