## DATABASE --> DATA --> TRAIN_TEST_SPLIT

import os
import sys
from src.CompleteDataScienceProject.exception import CustomException
from src.CompleteDataScienceProject.logger import logging
import pandas as pd
from src.CompleteDataScienceProject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            df = read_sql_data()
            logging.info("Reading completed mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_df, test_df = train_test_split(df , test_size=0.3 , random_state=0)
            train_df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data Ingestion Completed")

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)