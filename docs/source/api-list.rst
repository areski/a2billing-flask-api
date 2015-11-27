
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



Call - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of calls, create new calls, Update/Delete existing calls.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/call/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/call/?field=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/call/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/call/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{...}' http://localhost:8008/api/call/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{...}' http://localhost:8008/api/call/3/



CallerID - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of CallerIds, create new CallerIds, Update/Delete existing CallerIds.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/callerid/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/callerid/?field=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/callerid/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/callerid/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{...}' http://localhost:8008/api/callerid/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{...}' http://localhost:8008/api/callerid/3/



LogRefill - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of Refills, create new Refills, Update/Delete existing Refills.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/logrefill/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/logrefill/?field=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/logrefill/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/logrefill/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{...}' http://localhost:8008/api/logrefill/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{...}' http://localhost:8008/api/logrefill/3/



LogPayment - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of Payments, create new Payments, Update/Delete existing Payments.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/logpayment/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/logpayment/?field=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/logpayment/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/logpayment/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{...}' http://localhost:8008/api/logpayment/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{...}' http://localhost:8008/api/logpayment/3/


Country - Method [GET/POST/PUT/DELETE]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get list of Countries, create new Countries, Update/Delete existing Countries.

METHODS:

    GET ALL: curl -u username:password http://localhost:8008/api/country/

    GET ALL FILTER: curl -u username:password 'http://localhost:8008/api/country/?field=1321546'

    GET ONE: curl -u username:password http://localhost:8008/api/country/1/

    DELETE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X DELETE http://localhost:8008/api/country/4/

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{...}' http://localhost:8008/api/country/

    UPDATE: curl -u username:password --dump-header - -H "Content-Type:application/json" -X PUT --data '{...}' http://localhost:8008/api/country/3/


Refill - Method [POST]
~~~~~~~~~~~~~~~~~~~~~~

Refill a card with a credit amount (value: Decimal). The card will be refilled,
then a logpayment and a logrefill will be added to log the refill

METHODS:

    ADD: curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"credit": 5}' http://localhost:8008/custom_api/refill/1
