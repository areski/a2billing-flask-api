
.. _usage-api-extra-charge:

Usage API - Extra Charge
~~~~~~~~~~~~~~~~~~~~~~~~

This API will decrement an Account/Card for a given amount (value: Decimal),
then a charge will also be added to log the transaction.

In the result, the current balance will be returned and the created Charge Id
will also be returned.


ADD
^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"amount": 5}' http://localhost:8008/custom_api/extra_charge/1

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 82
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 22:46:36 GMT

    {
      "amount": 5.0,
      "card_id": 1,
      "charge_id": 8,
      "current_balance": 6496.0
    }
