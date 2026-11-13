from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hi Buddy, Welcome to the Arena!"