from fastapi import FastAPI
from products import products
import uvicorn

app = FastAPI()
# uvicorn main: app - -reload
# uvicorn main: app - -host 0.0.0.0 - -port 80 - -reload

@app.get('/')
async def home():
    return {"message": "Welcome to FastAPI tutorial!"}


# @app.get('/product')
# async def product_list():
#     return products
    

@app.get("/product/{product_id}")
async def product_view(product_id:int):
    for prod in products:
        if prod.get('id') == product_id:
            return {"message":"Product Available", "product":prod}
    return {"message":"Product Not Found"}