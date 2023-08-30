Python
=====

.. _installation:

Installation
------------

To use Hikerapi, first install it using pip:

.. code-block:: console

   $ pip install hikerapi

Usage
------------

You need to pass the key to the Client and call the function you want to get the result

For example:

>>> from hikerapi import Client
>>> cl = Client(api_key="")
>>> cl.user_a1("user")

or

>>> from hikerapi import AsyncClient
>>> cl = AsyncClient(api_key="")
>>> await cl.user_a1("user")


Class Methods
---------------

.. automodule:: hikerapi
   :members:
   :undoc-members:
   :show-inheritance:
