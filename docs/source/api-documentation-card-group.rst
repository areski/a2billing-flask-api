
.. _usage-api-card-group:

Usage API - Card Group
~~~~~~~~~~~~~~~~~~~~~~

Card Group allows to regroup Card per entity and define agents associated
to them, as well as user permissions when accessing the Customer UI.


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/cardgroup/

Result::

    {
        "meta": {
            "model": "cardgroup",
            "next": "",
            "page": 1,
            "previous": ""
        },
        "objects": [
            {
                "id_agent": null,
                "description": "This group is the default group used when you create a customer. It's forbidden to delete it because you need at least one group but you can edit it.",
                "users_perms": 262142,
                "id": 1,
                "name": "DEFAULT"
            },
            {
                "id_agent": 0,
                "description": null,
                "users_perms": 0,
                "id": 2,
                "name": "NewGroup"
            }
        ]
    }


GET ONE
^^^^^^^

$ curl -u username:password http://localhost:8008/api/cardgroup/1/

Result::

    {
        "id_agent": null,
        "description": "This group is the default group used when you create a customer. It's forbidden to delete it because you need at least one group but you can edit it.",
        "users_perms": 262142,
        "id": 1,
        "name": "DEFAULT"
    }


DELETE
^^^^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/cardgroup/4/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 18
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:11:03 GMT

    {
      "deleted": 1
    }


ADD
^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/cardgroup/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 96
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:08:55 GMT

    {
      "id_agent": 0,
      "description": "",
      "users_perms": 0,
      "id": 3,
      "name": "mygroup"
    }


UPDATE
^^^^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/cardgroup/3/

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 104
    Server: Werkzeug/0.9.4 Python/2.7.5+
    Date: Thu, 17 Apr 2014 16:12:31 GMT

    {
      "id_agent": 0,
      "description": "",
      "users_perms": 0,
      "id": 3,
      "name": "mygroup-updated"
    }
