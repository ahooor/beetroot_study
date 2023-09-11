from typing import Union
from fastapi import FastAPI
import json


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

file_path = "/Users/alisiyanosenko/Python/beetroot_study/practice/API/items.json"

def load_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# @app.post("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

api_url = "http://127.0.0.1:8000/"
