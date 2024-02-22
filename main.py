from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline

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