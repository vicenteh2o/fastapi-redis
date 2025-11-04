from fastapi import FastAPI
import requests
import redis
import json

rd = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/rick-morty/{character_id}")
def read_character(character_id: int):
    cache = rd.get(character_id)
    if cache:
        print("Cache hit")
        return json.loads(cache)
    else:
        print("Cache miss")
        r = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
        rd.set(character_id, r.text)
        rd.expire(character_id, 5)  # Cache expires in 1 hour (3600 seconds)
        return r.json()