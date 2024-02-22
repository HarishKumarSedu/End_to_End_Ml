from src.mlProject.entity.config_entity import(DataIngestionConfig,
                                               DataValidationConfig,
                                               DataTransformationConfig,
                                               ModelTrainConfig,
                                               ModelEvaluationConfig)
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
    
    def get_data_validation_config(self)->DataValidationConfig:
        
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation = DataValidationConfig(
            root_dir        = config.root_dir,      
            unzip_data_dir  = config.unzip_data_dir,
            STATUS_FILE     = config.STATUS_FILE,
            all_schema      = schema
        )
        return data_validation
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path
        )
        return data_transformation
    
    def get_model_trainer_config(self)->ModelTrainConfig:
        config = self.config.model_trainer
        target = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet
        create_directories([config.root_dir])
        
        model_trainer = ModelTrainConfig(
                    root_dir            = config.root_dir  ,
                    train_data_path     = config.train_data_path,
                    test_data_path      = config.test_data_path,
                    model_name          = config.model_name,
                    alpha               = params.alpha,
                    l1_ratio            = params.l1_ratio,
                    target_column       = target.name,
        )
        
        return model_trainer
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        model_evaluvation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            model_path= config.model_path, 
            metric_file_name=config.metric_file_name,
            target_column= schema.name,
            all_params=params,
            mlflow_uri="http://127.0.0.1:5000/#/experiments/203287971472228066?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All%20Runs&selectedColumns=attributes.%60Source%60,attributes.%60Models%60&isComparingRuns=false&compareRunCharts=dW5kZWZpbmVk",
        ) 
        
        return model_evaluvation_config