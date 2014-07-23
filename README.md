###Setup

#### Env variables

As you may have seen in the conf.py file, 3 variables ar needed to use the Iceperg python API: the Iceberg private key, the Iceberg secret key and the application namespace. These variables must be initiated as environment variables. For security purposes we're gonna load them in a seperate file. Let's create a env.sh file in the root folder containing the following lines.

```python

export ICEBERG_API_PRIVATE_KEY=XXXXXX
export ICEBERG_APPLICATION_NAMESPACE=my_app
export ICEBERG_APPLICATION_SECRET_KEY=XXXXXX

```

Theses variables must now be loaded in the environment using 
<pre>source env_setup.sh</pre>

#### Log in 

For many of the API operations, we need to be logged in as a user (as a staff user or not). So let's create a logIn function we are gonna call everytime we need to.

```python

api_handler = IcebergAPI()
api_handler.sso("userEmail","userFirstName","userLastName")
return api_handler

```
* * *

#### Get infos of a specific offer

Let's fetch some specific informations about an offer, display the image url, description, and get stock, size and price for each variation. 

```python

#fetch offer object width the product ID
product = api_handler.ProductOffer.find("52")

#print infos
print product.default_image_url
print product.description
for variation in product.variations:
    print "%s items available in size %s, %s euros" %(variation['stock'],variation['name'],variation['price'])

```
* * *

#### Add product to cart

These few lines of code show you how to simply add a product to a specific user's cart, don't forget to pass the 4 required arguments.

```python

#Get cart
user_cart = api_handler.Cart.mine()

#fetch offer object width the product ID
product = api_handler.ProductOffer.find("52")

#print propreties of the product you just found
print product.description
print product.price_with_vat

#Add offer to the logged user's cart
user_cart.addOffer(product)

#print total amount of the cart
print api_handler.Cart.mine().total_amount
    
```
* * *


#### Get infos of a user's cart

Let's retrieve a user's cart object and display its shipping_adress, shipping amount and total amount.

```python

#cart object
user_cart = api_handler.Cart.mine()

#print infos
print user_cart.shipping_address
print user_cart.shipping_amount
print user_cart.total_amount
    
```
* * *


#### Get user infos

Retrieve specific infos about a user

```python

me = api_handler.User.me()

#print me.to_JSON()
print me.username
print me.first_name
print me.last_name
print me.email
print me.timezone

```
* * *


#### Get store infos

Retrieve infos about a store in the application. We are gonna look for the store number 11 and display infos about it. This number is allocated automatically by Iceberg, you can find your stores's IDs in the get request's response on the "merchant" section.

```python

store = api_handler.Store.find(11)

print store.name
print store.created_on
print store.long_description
print store.url

```


