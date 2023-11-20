#from src.CompleteDataScienceProject import logger
from src.CompleteDataScienceProject.logger import logging
from src.CompleteDataScienceProject.exception import CustomException
import sys
from src.CompleteDataScienceProject.components.data_ingestion import DataIngestion,DataIngestionConfig

if __name__ == "__main__":
    ## logging.INFO("YOYOYOYO HONEY SINGH")
    logging.info("YOYOYOYO HONEY SINGH")

    try:
        #a= 1/0
        #dataingestionconfig = DataIngestionConfig()
        #dataingestion = DataIngestion(a)

        dataingestion = DataIngestion()
        train_data_path , test_data_path = dataingestion.initiate_data_ingestion()
        


    except Exception as e:
        #logging.info("Error Message/ Name - {}".format(e))
        #logging.info("Error Details - {}".format(sys))
        raise CustomException(e,sys)