Timeout Information
===================================

Dear HikerAPI customers!

Please note that each HikerAPI client has a limit of approximately 1 million requests per day, which is equivalent to 15 requests per second.

In case you are getting the 429 Too Many Requests error, we recommend changing the “timeout” parameter in your code. An example of the timeout setting is shown below:

.. code-block:: python

    import requests

    # Set headers for authorization and for specifying the type of expected response
    headers = {
        "x-access-key": "<your token>",  # Replace <your token> with your access token
        "accept": "application/json"
    }

    # Initial query parameters
    params = {
        "user_id": '123123',  # User ID
        "page_id": None  # Page ID for pagination
    }

    followers = []  # A list for storing users subscribed to by a given user

    # Cycle to retrieve all user subscriptions using pagination
    while True:
        # Execute GET request to API with specified headers and parameters
        response = requests.get(
            "https://api.hikerapi.com/v2/user/following",
            headers=headers,
            params=params,
            timeout=15  # Set a timeout of 15 seconds.
        )
        
        # Convert the response to JSON and extract values
        r = response.json().values()
        
        # Retrieve the list of users and the ID of the next page
        res, params["page_id"] = r
        
        # Add the received users to the list
        followers.extend(res['users'])
        
        # Check if we have reached the end of the list (no next page)
        if params['page_id'] is None or params['page_id'] == 0:
            break

    # The followers list now contains all of the user's subscriptions
    print(followers)


This approach will help you avoid exceeding limits and ensure the stability of your applications.

Thank you for your attention and cooperation.

Regards,
HikerAPI Support Team

