### ======================================== DAY - 1 ========================================
from fastapi import FastAPI
from enum import Enum
from .products import products

app = FastAPI()

class Category(str, Enum):
    MOBILE = "Mobile"
    FASHION = "Fashion"
    HOME = "Home"
    ELECTRONICS = "Electronics"


@app.get('/')
async def home():
    return {"message": "Welcome to FastAPI day-1."}

## ------------------ Topic :: Order Matters ------------------
# Wrong order.
# @app.get('/greet/{name}')
# async def greet_user(name):
#     return {'message': f'Good morning! {name}.'}

# @app.get('/greet/welcome')
# async def welcome():
#     return {"message", "This will welcome message."}
    
## Correct Order
@app.get('/greet/welcome')
async def welcome():
    return {"message": "This is welcome message."}
    
## ------------------ Topic :: Path Parameters ------------------
@app.get('/greet/{name}')
async def greet_user(name):
    return {'message': f'Good morning! {name}.'}


## ------------------ Topic :: Type Conversion ------------------
@app.get('/item/{price}')
async def product(price:float):
    print(f"Price : {price} & Type : {type(price)}")
    return {"Item Price":price, "message":"Price is in float."}


## ------------------ Topic :: Multiple Path Parameters ---------
@app.get('/user/{user_id}/post/{post_id}')
async def get_post_by_user(user_id:int, post_id:int):
    return {"user_id":user_id, "post_id":post_id}


## ------------------ Topic :: Path Converter ---------
# @app.get('/files/{file_path}') # dev/test/main.py - Error: Not Found
# or : dev\test\main.py - "file_path": "dev\\test\\main.py", 
@app.get('/files/{file_path:path}') # dev\test\main.py -- "dev\\test\\main.py"
async def read_file(file_path:str):
    return {"file_path":file_path, "message":"File is read completely."}

## ------------------ Topic :: Using Enum ---------
@app.get('/product/{category}')
async def product_by_category(category:Category):
    filtered_product = []
    # print(f"Name : {category.name} & value : {category.value}")
    for prod in products:
        if prod.get('category') == category.value:
            filtered_product.append(prod)

    return {"products": filtered_product}
### ======================================== DAY - 1 ========================================
from fastapi import FastAPI
from enum import Enum
from .products import products

app = FastAPI()

class Category(str, Enum):
    MOBILE = "Mobile"
    FASHION = "Fashion"
    HOME = "Home"
    ELECTRONICS = "Electronics"


@app.get('/')
async def home():
    return {"message": "Welcome to FastAPI day-1."}

## ------------------ Topic :: Order Matters ------------------
# Wrong order.
# @app.get('/greet/{name}')
# async def greet_user(name):
#     return {'message': f'Good morning! {name}.'}

# @app.get('/greet/welcome')
# async def welcome():
#     return {"message", "This will welcome message."}
    
## Correct Order
@app.get('/greet/welcome')
async def welcome():
    return {"message": "This is welcome message."}
    
## ------------------ Topic :: Path Parameters ------------------
@app.get('/greet/{name}')
async def greet_user(name):
    return {'message': f'Good morning! {name}.'}


## ------------------ Topic :: Type Conversion ------------------
@app.get('/item/{price}')
async def product(price:float):
    print(f"Price : {price} & Type : {type(price)}")
    return {"Item Price":price, "message":"Price is in float."}


## ------------------ Topic :: Multiple Path Parameters ---------
@app.get('/user/{user_id}/post/{post_id}')
async def get_post_by_user(user_id:int, post_id:int):
    return {"user_id":user_id, "post_id":post_id}


## ------------------ Topic :: Path Converter ---------
# @app.get('/files/{file_path}') # dev/test/main.py - Error: Not Found
# or : dev\test\main.py - "file_path": "dev\\test\\main.py", 
@app.get('/files/{file_path:path}') # dev\test\main.py -- "dev\\test\\main.py"
async def read_file(file_path:str):
    return {"file_path":file_path, "message":"File is read completely."}

## ------------------ Topic :: Using Enum ---------
@app.get('/product/{category}')
async def product_by_category(category:Category):
    filtered_product = []
    # print(f"Name : {category.name} & value : {category.value}")
    for prod in products:
        if prod.get('category') == category.value:
            filtered_product.append(prod)

    return {"products": filtered_product}
