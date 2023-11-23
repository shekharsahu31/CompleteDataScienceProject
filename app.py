#from src.CompleteDataScienceProject import logger
from src.CompleteDataScienceProject.logger import logging
from src.CompleteDataScienceProject.exception import CustomException
import sys
from src.CompleteDataScienceProject.components.data_ingestion import DataIngestion,DataIngestionConfig
from dotenv import load_dotenv
import os
import pandas as pd
from src.CompleteDataScienceProject.components.data_transformation import DataTransformationConfig, DataTransformation
from src.CompleteDataScienceProject.components.model_tranier import Model_trainer, ModelTrainerConfig


if __name__ == "__main__":
    ## logging.INFO("YOYOYOYO HONEY SINGH")
    logging.info("YOYOYOYO HONEY SINGH")

    try:
        #a= 1/0
        #dataingestionconfig = DataIngestionConfig()
        #dataingestion = DataIngestion(a)

        dataingestion = DataIngestion()
        raw_data_path , train_data_path , test_data_path = dataingestion.initiate_data_ingestion()
        '''print(train_data_path)
        print(test_data_path)
        df = pd.read_csv(train_data_path)
        print(df.info())'''
        datatransf = DataTransformation()
        train_arr,test_arr,trandformer_pickle_file_path = datatransf.initiate_data_transformation(raw_data_path , train_data_path , test_data_path)
        #print(trandformer_pickle_file_path)
        modeltrainer=Model_trainer()
        modeltrainer.initiate_model_trainer(train_arr,test_arr)


    except Exception as e:
        #logging.info("Error Message/ Name - {}".format(e))
        #logging.info("Error Details - {}".format(sys))
        raise CustomException(e,sys)
    