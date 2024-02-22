import os 
import urllib.request as request 
import zipfile
from src.mlProject.utils.common import get_size
from pathlib import Path
from src.mlProject.entity.config_entity import (DataIngestionConfig)
from src.mlProject import logger

class DataIngestion:
    
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config = config
        
        
    def download_file(self):
        
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url= self.config.source_url,
                filename=self.config.local_data_file
            )
            
            logger.info(f'{filename} downloaded! with the following info: \n{header}')
        else:
            logger.info(f'File Already Exists of size: { get_size(Path(self.config.local_data_file))}')
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)