Timeout Information
===================================

.. container:: note

   Dear HikerAPI Customer

   Default request volume (which could be increased) is 1 million requests per day, which is equivalent to 11 requests per second. To manage your requests more accurately, it is important to keep in mind that this equates to approximately 11 requests per second to perfectly meet your daily limit. If the number of requests exceeds this figure, you may encounter a 429 (Too Many Requests) error, which will temporarily restrict your access to the API. This may affect the total amount of data you can collect in a day, as you will have to wait for the request limits to be lifted.

   To avoid such situations, we recommend that you monitor the frequency of requests and adjust the number of requests if necessary to ensure that your system runs smoothly and our resources are utilized efficiently.

   Regards,  
   HikerAPI Team

Example

.. code-block:: python

   import time
   import asyncio
   import aiohttp

   users_ids = ["1553030189", "12345"]
   all_followers = []


   async def get_followers(user_id):
      async with aiohttp.ClientSession() as session:
         headers = {
               "x-access-key": "1AvYIfJM1lepy5HE4U22ZYZIvHcJ4ygs",
               "accept": "application/json"
         }

         params = {
               "user_id": user_id,
               "page_id": ""
         }

         url = "https://api.hikerapi.com/v2/user/followers"
         followers = []
         rate_limit = 11
         delay = 1 / rate_limit

         while True:
               start_time = time.time()
               async with session.get(url=url, params=params, headers=headers) as response:
                  res = await response.json()
                  users, page_id = res["response"]["users"], res["next_page_id"]
                  followers.extend(users)

                  if not page_id:
                     break

                  params["page_id"] = page_id
                  cycle_time = time.time() - start_time
                  sleep_time = max(0, delay - cycle_time)
                  await asyncio.sleep(sleep_time)

      return followers


   async def main():
      tasks = [asyncio.create_task(get_followers(user_id)) for user_id in users_ids]

      results = await asyncio.gather(*tasks)

      for result in results:
         all_followers.extend(result)


   asyncio.run(main())