# Order Place API Support:

  A Simple System to place the order with the following details
  1. Order_items
  2. Distance of the user in meter 
  3. Offer, if applicable
  

## Run Application without Docker

```
$ Virtualenv env -p python3
$ source ~/env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver

$ POST - http://localhost:8000/order/
```


## Run Application with Docker

```
$ docker build --tag esamudaayorder .
$ docker run --publish 8000:8000 esamudaayorder

$ POST - http://localhost:8000/order/
```

## Run All UnitTestCase

```
$ Virtualenv env -p python3
$ source ~/env/bin/activate
$ python manage.py test
```
 
## Operations Allowed

 ## Place Order
 http://localhost:8000/Post/
 
 ## Input
 {
  "order_items": [
    {
      "name": "bread",
      "quantity": 2,
      "price": 2200
    },
    {
      "name": "butter",
      "quantity": 1,
      "price": 5900
    }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "FLAT",
    "offer_val": 1000
  }
 }
 
 ## Response
 {'order_total':14300}