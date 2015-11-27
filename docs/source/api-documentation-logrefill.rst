
.. _usage-api-logrefill:

Usage API - Logrefill
~~~~~~~~~~~~~~~~~~~~~

This is used to track the refill made into the A2Billing platform.


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/logrefill/

Result::

    {
      "meta": {
        "model": "logrefill",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "description": "CREATION CARD REFILL",
          "refill_type": 0,
          "agent": null,
          "credit": 5.00000,
          "date": "2014-04-16 01:11:45",
          "id": 1,
          "card": 1,
          "added_invoice": 0
        },
        {
          "description": "4654",
          "refill_type": 0,
          "agent": null,
          "credit": 6456.00000,
          "date": "2014-06-04 14:56:36",
          "id": 2,
          "card": 1,
          "added_invoice": 0
        },
      ]
    }


GET ONE
^^^^^^^

TODO: Not documented!


DELETE
^^^^^^

TODO: Not documented!


ADD
^^^

TODO: Not documented!


UPDATE
^^^^^^

TODO: Not documented!
