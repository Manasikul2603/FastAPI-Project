from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get('/Hello')
def hello():
    return JSONResponse({'message':'Hello World'}, status_code=200)