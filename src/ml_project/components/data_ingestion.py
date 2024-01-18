# sql - data_ingestion- test_train_split
import os 
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import  custom_exception
import pandas as pd 
from dataclasses import dataclass
from src.ml_project.utils import read_data 
from sklearn.model_selection import train_test_split

#This is a configuration class using the @dataclass decorator.
# It sets default file paths for training, testing, and raw data.

@dataclass 

class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
    
    

# This is a class responsible for ingesting data.
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  
    
# This method initiates the data ingestion process.
    def data_ingestion_initialization(self):
        try:
            df = read_data()
            logging.info("reading data from mysql")

            #create dir for file path  Ensure the directory structure for the output files exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path))
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header= True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state= 42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header= True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header= True)
            logging.info("data ingestion completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )


        except Exception as ex:
            raise custom_exception(ex,sys)
    
    