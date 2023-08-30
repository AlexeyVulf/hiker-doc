Getting Started
===================================

.. _installation:

First Steps
------------------------------------

With Hikerapi, you have several options to use it. 
You can handle your needs with our API `Hikerapi SaaS <https://hikerapi.com/p/894GyDoD>`_,
or use our :ref:`Python library <Python>`.

.. code-block:: console

   $ pip install hikerapi

Trial version
------------------------------------

Have a trial by a following link `hikerapi SaaS <https://hikerapi.com/p/894GyDoD>`_

A demonstration of an example
------------------------------------

In order to show what hikerapi brings into the table, 
we'll walk you through an example of a Python-hikerapi usage.


.. code-block:: python

    from hikerapi import Client

    cl = Client(token="<your_token_here>")

    def get_followers(cl, user_id):
        followers = {}
        followers_len = -1
        end_cursor = None
        while len(followers) > followers_len:
            followers_len = len(followers)
            res, end_cursor = cl.user_followers_chunk_gql(user_id=user_id, end_cursor=end_cursor)
            followers.update({item['pk']:item for item in res})
        return list(followers.values())

    followers = get_followers(cl, "12345678")

or achieve the same effect with API calls using Python requests

.. code-block:: python

    import requests

    headers = {"x-access-key": "<your_token_here>","accept": "application/json"}
    def get_followers(user_id, url):
        followers = {}
        followers_len = -1
        params = {"user_id":user_id, "end_cursor":None}
        while len(followers) > followers_len:
            followers_len = len(followers)
            res, params["end_cursor"] = requests.get(url, headers=headers, params=params).json()
            followers.update({item['pk']:item for item in res})
        return list(followers.values())

    followers = get_followers("12345678", "https://api.hikerapi.com/gql/user/followers/chunk")

Example of writing into a file.
------------------------------------

.. code-block:: python

    import aiofiles
    from aiocsv import AsyncWriter
    from hikerapi import AsyncClient

    columns = [
        "pk",
        "username",
        "full_name",
        "is_private",
        "is_verified",
        "media_count",
        "follower_count",
        "following_count",
        "biography",
        "external_url",
        "is_business",
        "public_email",
        "contact_phone_number",
    ]
    ids = ["123456", "12345"]
    cl = AsyncClient(token="<your_token_here>")


    def create_row(res: dict, columns: list) -> list:
        for key in res.copy():
            if key not in columns:
                del res[key]
        return list(res.values())


    async with aiofiles.open("user_info.csv", "w") as f:
        writer = AsyncWriter(f)
        await writer.writerow(columns)
        for id_ in ids:
            res = await cl.user_by_id_v1(id_)
            row = create_row(res, columns)
            await writer.writerow(row)

If you don't have a user_id, you can get one by doing the following. 

.. code-block:: python

    res = cl.user_a1("v_n.www")
    res["graphql"]["user"]["id"]

or by endpoint /a1/user?username=...

`hikerapi Swagger UI <https://hikerapi.com/tokens>`_

https://api.hikerapi.com/a1/user?username=ronaldo


What just happened?
------------------------------------

The user's followers have been successfully extracted and organized into a list/csv. 

This allows for easy access and analysis of the data, 
as well as potential for further processing such as sorting by various 
criteria or filtering out interesting accounts. 

With this information, 
the user may gain insights into their audience and identify potential 
new followers or target demographics.



