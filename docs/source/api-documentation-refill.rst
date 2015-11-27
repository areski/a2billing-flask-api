
.. _usage-api-refill:

Usage API - Refill
~~~~~~~~~~~~~~~~~~

This API will refill an Account/Card for a given credit amount (value: Decimal).
A logpayment and a logrefill will also be added to log the refill.

In the result, the current balance will be returned with the VAT/Tax from the
Account/Card, and the created logpayment ID and logrefill Id will also be returned.


ADD
^^^

$ curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"credit": 5}' http://localhost:8008/custom_api/refill/1

Result::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 169
    Server: Werkzeug/0.11.2 Python/2.7.9
    Date: Fri, 27 Nov 2015 22:04:31 GMT

    {
      "card_id": 1,
      "credit_without_vat": 5.0,
      "credited": 5.0,
      "current_balance": 6511.0,
      "logpayment_id": 9,
      "logrefill_id": 19
      "vat": 0
    }
