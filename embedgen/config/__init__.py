import os
import sys
from embedgen.utils.common import read_yaml
# from project_store_exception_layer.exception import CustomException as ConfigurationException
from embedgen.exception import DocumentException


class Configuration:
    def __init__(self):
        try:
            config = read_yaml(os.path.join("configs", "config.yaml"))

            artifacts = config['artifacts']

            self.artifacts_dir = artifacts['artifacts_dir']
            self.input_path = artifacts['input_path']
            self.input_file = artifacts['input_file']
            self.detector_backend = artifacts['detector_backend']
            self.embedding_model = artifacts['embedding_model']
            self.target_size = artifacts['target_size']
        except Exception as e:
            raise DocumentException(e, sys) from e
