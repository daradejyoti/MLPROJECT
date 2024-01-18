from src.ml_project.logger import logging
from src.ml_project.exception import  custom_exception
import sys
from src.ml_project.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__ == "__main__":
    logging.info("started")


    try:
       data_ingestion1 = DataIngestion()
       logging.info ("data ingestion now started")
       data_ingestion1.data_ingestion_initialization()

       logging.info ("data ingestion completed")

    except Exception as e :
       logging.info("EXCEPTION")
       raise  custom_exception(e,sys)