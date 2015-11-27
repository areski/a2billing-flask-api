
.. _usage-api-country:

Usage API - Country
~~~~~~~~~~~~~~~~~~~

List of countries.


GET ALL
^^^^^^^

$ curl -u username:password http://localhost:8008/api/country/

Result::

    {
      "meta": {
        "model": "country",
        "next": "/api/country/?page=2",
        "page": 1,
        "previous": ""
      },
      "objects": [
        {
          "countryname": "Afghanistan",
          "id": 1,
          "countrycode": "AFG",
          "countryprefix": "93"
        },
        {
          "countryname": "Albania",
          "id": 2,
          "countrycode": "ALB",
          "countryprefix": "355"
        },
      ...
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
