import sys
import os
import io
import logging
import numpy as np
from PIL import Image
from embedgen.utils.common import read_yaml, create_directories, decodeImage, encodeImageIntoBase64
from embedgen.config import Configuration
from embedgen.exception import DocumentException
from deepface import DeepFace


os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

ROOT = os.getcwd()
STAGE = "Embedding generator" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )
class Embedding:
    def __init__(self, image_path: bytes):
        try:
            self.image_path = image_path
            # language will be a hyperparameter
            self.config = Configuration()
        except Exception as e:
            raise DocumentException(e, sys) from e
    def generate_embedding(self):
        try:
            input_image_path = os.path.join(self.config.artifacts_dir, self.config.input_path, self.config.input_file)
            input_image_file = Image.open(io.BytesIO(self.image_path)).convert('RGB')
            input_image_file.save(os.path.join(ROOT, input_image_path))
            input_image_array = np.array(input_image_file)

            face = DeepFace.detectFace(img_path = input_image_array, 
                    target_size = (224, 224),
                    detector_backend = self.config.detector_backend
            )

            embedding = DeepFace.represent(img_path = face, 
            model_name = self.config.embedding_model, enforce_detection=False,
            )
            return embedding
        
        except Exception as e:
            raise DocumentException(e, sys) from e

