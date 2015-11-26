
.. _list-apis:

List of APIs
------------

This is the list of Restful APIs supported.

CardGroup - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of card-groups, create new card-group, Update/Delete existing card-group.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/cardgroup/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/cardgroup/?name=DEFAULT'

    GET ONE: curl -u username:password http://localhost:8008/api/cardgroup/1

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/cardgroup/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/cardgroup/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/cardgroup/3/


Card - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of cards, create new card, Update/Delete existing card.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/card/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/card/?username=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/card/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/card/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "mygroup", "description": ""}' http://localhost:8008/api/card/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{"name": "mygroup-updated", "description": ""}' http://localhost:8008/api/card/3/
