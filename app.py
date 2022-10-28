from distutils.log import debug
from embedgen.component.embed import Embedding
from embedgen.exception import DocumentException

import uvicorn
from typing import Optional
from fastapi import APIRouter, File, Request, FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/via_postman")
async def image_response(image_file: bytes = File(...)):
    try:
        embedding_generator = Embedding(image_file)
        embeddings = embedding_generator.generate_embedding()
        response =  JSONResponse(content = {"embeddings": embeddings}, status_code=200)
        return response
    except DocumentException as e:
        return e

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port = 5000)