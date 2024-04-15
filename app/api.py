# main.py
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Set up CORS
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)




@app.get("/{exchange}/{ticker}")
async def read_user_item(ticker: str, exchange: str):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    classl = "YMlKec fxKbKc"
    price = float(soup.find(class_=classl).text.strip()[1:].replace(",",""))
    return {"nav":price}