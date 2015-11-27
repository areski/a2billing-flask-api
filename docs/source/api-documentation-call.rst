
.. _usage-api-call:

Usage API - Call
~~~~~~~~~~~~~~~~

This entity is the Call, also known as CDR.


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/call/

Result::

    {
      "meta": {
        "model": "call",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "calledstation": "7987944994",
          "id_did": 0,
          "id_tariffplan": 1,
          "id": 1,
          "id_ratecard": 1,
          "terminatecauseid": 5,
          "destination": 132487987,
          "dnid": "61984644",
          "starttime": "2015-11-27 22:36:02",
          "id_card_package_offer": 0,
          "nasipaddress": "127.0.0.1",
          "id_trunk": 2,
          "sipiax": null,
          "sessionid": "13564654984",
          "stoptime": null,
          "sessiontime": 40,
          "uniqueid": "654654981615",
          "src": "source",
          "buycost": 0.10000,
          "card_id": 1,
          "id_tariffgroup": 2,
          "real_sessiontime": 50,
          "sessionbill": 40.0
        }
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
