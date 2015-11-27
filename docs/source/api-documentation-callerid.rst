
.. _usage-api-callerid:

Usage API - Callerid
~~~~~~~~~~~~~~~~~~~~

This entity is the CallerIDs associated to a customer (Card)


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/cardgroup/

Result::

    {
      "meta": {
        "model": "callerid",
        "next": "",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "id_cc_card": 1,
          "activated": "t",
          "id": 2,
          "cid": "45454565456456"
        }
      ]
    }



GET ONE
^^^^^^^

$ curl -i -u username:password http://localhost:8008/api/cardgroup/1/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 79
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 21:27:56 GMT

    {
      "id_cc_card": 1,
      "activated": "t",
      "id": 2,
      "cid": "45454565456456"
    }


DELETE
^^^^^^

$ curl -u username:password  --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/callerid/6/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 18
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 21:29:18 GMT

    {
      "deleted": 1
    }


ADD
^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"id_cc_card": 1, "cid": "9501234657"}' http://localhost:8008/api/callerid/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 75
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 21:31:19 GMT

    {
      "id_cc_card": 1,
      "activated": "t",
      "id": 7,
      "cid": "9501234657"
    }


UPDATE
^^^^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"cid": "9501234658"}' http://localhost:8008/api/callerid/7/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 75
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 21:32:30 GMT

    {
      "id_cc_card": 1,
      "activated": "t",
      "id": 7,
      "cid": "9501234658"
    }
