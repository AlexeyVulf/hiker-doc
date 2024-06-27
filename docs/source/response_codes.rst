Response Codes
===================================

.. list-table::
   :header-rows: 1
   :widths: 10 20 70

   * - Code
     - Description
     - HikerAPI Description
   * - 200
     - OK
     - The Request Has Succeeded
   * - 307
     - Temporary Redirect
     - | The requested resource is temporarily available
       | at a different URL
   * - 400
     - Bad Request
     - Arguments are not correctly transmitted
   * - 401
     - Unauthorized
     - You forgot to add the token to the query
   * - 402
     - Payment Required
     - Payment is required to access HikerAPI
   * - 403
     - Forbidden
     - The account/comment/media is private
   * - 404
     - Not Found
     - The Account/comment/media not found
   * - 405
     - Method Not Allowed
     - This HTTP method is not allowed for HikerAPI
   * - 408
     - Requests Timeout
     - | The server waited too long for the request 
       | and closed the connection,
       | maybe because of bad internet connection.
   * - 422
     - Unprocessable Entity
     - | The server understands the request
       | but cannot process it due to semantic errors
   * - 429
     - Too Many Requests
     - | Your request was rejected due
       | to exceeding the request limit
   * - 430
     - Request Header Fields Too Large
     - Request Header Fields Too Large
   * - 500
     - Internal Server Error
     - | There was an internal error on the server
       | while processing your request
       | (request fee is not charged)
   * - 503
     - Service Unavailable
     - | The server is temporarily unable to process
       | requests due to temporary overloading
       | (request fee is not charged)
   * - 504
     - Gateway Timeout
     - | Network delays or server access problems
       | (request fee is not charged)