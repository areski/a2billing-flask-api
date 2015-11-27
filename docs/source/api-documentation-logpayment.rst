
.. _usage-api-logpayment:

Usage API - Logpayment
~~~~~~~~~~~~~~~~~~~~~~

This is used to track the payment made into the A2Billing platform.


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/logpayment/

Result::

    {
      "meta": {
        "model": "logpayment",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "added_refill": 1,
          "description": "4654",
          "added_commission": 0,
          "id": 1,
          "payment_type": 2,
          "agent": null,
          "date": "2014-06-04 14:56:36",
          "id_logrefill": 2,
          "payment": 6456.00000,
          "card": 1
        },
        {
          "added_refill": 0,
          "description": null,
          "added_commission": 0,
          "id": 2,
          "payment_type": 0,
          "agent": null,
          "date": null,
          "id_logrefill": 12,
          "payment": 5.89000,
          "card": 2
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
