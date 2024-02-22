from src.mlProject.entity.config_entity import DataIngestionConfig
from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml,create_directories,get_size

class ConfigurationManager:
    
    def __init__(self,
                 config_filepath=CONFIG_PATH,
                 params_filepath=PARAMS_PATH,
                 schema_filepath=SCHEMA_PATH,
                 ) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        data_ingestion = DataIngestionConfig(
            root_dir        =   config.root_dir,
            source_url      =   config.source_url,
            local_data_file =   config.local_data_file,
            unzip_dir       =   config.unzip_dir,
        )
        
        return data_ingestion