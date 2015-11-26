
.. _usage-api-card:

Usage API - Card
~~~~~~~~~~~~~~~~

Cards are A2Billing Users on the A2Billing Platform, this regroups credentials and specific information related to
the users, such as names, address, balance, etc..


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/card/

Result::

    {
        "meta": {
          "model": "card",
          "next": "",
          "page": 1,
          "previous": ""
        },
        "objects": [
          {
            "email_notification": "areski@gmail.com",
            "status": 1,
            "expiredays": null,
            "loginkey": "4654",
            "lock_pin": "0",
            "useralias": "312224525577965",
            "uipass": "18314euvyzix7spr1eew",
            "activated": "f",
            "currency": "USD",
            "tag": "ok",
            "initialbalance": 0.0,
            "voicemail_activated": 0,
            ...,
            ...
          }
        ]
    }


GET ONE
^^^^^^^

$ curl -u username:password http://localhost:8008/api/card/1/

Result::

    {
      "email_notification": "areski@gmail.com",
      "status": 1,
      "expiredays": null,
      "loginkey": "4654",
      "lock_pin": "0",
      "useralias": "312224525577965",
      "uipass": "18314euvyzix7spr1eew",
      "activated": "f",
      "currency": "USD",
      "tag": "ok",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "0",
      "id": 1,
      "sip_buddy": 1,
      "city": "Barcelona",
      "id_group": 1,
      ...,
    }


DELETE
^^^^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/card/4/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 18
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 18:50:43 GMT

    {
      "deleted": 1
    }


ADD
^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"username": "1234567890", "useralias": "0554654648", "lastname": "Belaid", "firstname": "Areski", "uipass": "6546456", "credit": "5", "tariff": "1"}' http://localhost:8008/api/card/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1257
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 23:33:14 GMT

    {
      "email_notification": "",
      "status": 1,
      "expiredays": null,
      "loginkey": "",
      "lock_pin": null,
      "useralias": "0554654648",
      "uipass": "6546456",
      "activated": null,
      "currency": "USD",
      "tag": "",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "",
      "id": 7,
      "sip_buddy": 0,
      "city": "",
      "id_group": 1,
      "notify_email": 0,
      ...
    }


UPDATE
^^^^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"lastname": "Belaid"}' http://localhost:8008/api/card/7/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1290
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 23:36:10 GMT

    {
      "email_notification": "",
      "status": 1,
      "expiredays": "",
      "loginkey": "",
      "lock_pin": null,
      "useralias": "0554654648",
      "uipass": "6546456",
      "activated": "f",
      "currency": "USD",
      "tag": "",
      "initialbalance": 0.0,
      "voicemail_activated": 0,
      "redial": "",
      "id": 7,
      "sip_buddy": 0,
      "city": "",
      "id_group": 1,
      "notify_email": 0,
      ...
    }
