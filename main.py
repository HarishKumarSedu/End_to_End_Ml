from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation_pipline import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_04_model_trainer_pipeline import ModelTrainerTrainingPipeline

if __name__ == '__main__':
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    try:
        STAGE_NAME = "Data validation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    try:
        STAGE_NAME = "Data Transformation stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    try:
        STAGE_NAME = "Data Trainer stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e