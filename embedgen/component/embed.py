import sys
import os
import logging
from PIL import Image
from embedgen.utils.common import read_yaml, create_directories, decodeImage, encodeImageIntoBase64
from embedgen.config import Configuration
from embedgen.exception import DocumentException
from deepface import DeepFace

import cv2



ROOT = os.getcwd()
STAGE = "Embed generator" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )
class Embedding:
    def __init__(self, image_path):
        try:
            self.image_path = image_path
            # language will be a hyperparameter
            self.config = Configuration()
        except Exception as e:
            raise DocumentException(e, sys) from e
    def getOcrPrediction(self):
        try:
            face = DeepFace.detectFace(img_path = self.image_path, 
                    target_size = (224, 224), 
                    detector_backend = 'mtcnn'
            )

            embedding = DeepFace.represent(img_path = face, 
            model_name = 'Facenet', enforce_detection=False,
                )
            return embedding

        except Exception as e:
            raise DocumentException(e, sys) from e

