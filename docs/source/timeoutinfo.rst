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

   import asyncio
   import aiohttp

   users_ids = [
      "1553030189", "12345", "4238157586", "57606704380",
      "44207170437", "58568300401", "47857986514", "419762293",
      "11461087642", "5310983422", "25044994947", "25044994947",
      "6882128701", "37452706560", "420842043", "1220781192",
      "6388630183", "1320664128", "6438020799", "52027596085",
   ]

   rate_limit = 11
   url = "https://api.hikerapi.com/v2/user/followers"
   headers = {"x-access-key": "<your_token_here>", "accept": "application/json"}

   all_followers = []
   semaphore = asyncio.Semaphore(rate_limit)


   async def get_followers(user_id):
      async with semaphore:
         async with aiohttp.ClientSession() as session:
               params = {"user_id": user_id, "page_id": ""}
               followers = []

               while True:
                  async with session.get(url=url, params=params, headers=headers) as response:
                     res = await response.json()
                     users, page_id = res["response"]["users"], res["next_page_id"]
                     followers.extend(users)

                     if not page_id:
                           break

                     params["page_id"] = page_id
                     await asyncio.sleep(1/rate_limit)

      return followers


   async def main():
      tasks = [asyncio.create_task(get_followers(user_id)) for user_id in users_ids]
      results = await asyncio.gather(*tasks)
      all_followers.extend(result for result in results)

   asyncio.run(main())