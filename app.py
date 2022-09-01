from distutils.log import debug
from embedgen.component.embed import Embedding

from typing import Optional
from flask import Flask, request
app = Flask(__name__)


# Take input as image path and give json response
@app.route('/embedding', methods=["GET", 'POST'])
def image_response():
    if request.method == "POST":
        # get input as image path
        image_path = request.json["image_path"]
        embedding_generator = Embedding(str(image_path))
        embeddings = embedding_generator.getOcrPrediction()
        response =  {"embeddings": embeddings}
        return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000, debug=True)