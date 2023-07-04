from fastapi import FastAPI
import tensorflow as tf

app = FastAPI()   

@app.get("/") 
async def main_route():     
  return {
    "message": "Hey, It is me Goku"
  }
