#from src.CompleteDataScienceProject import logger
from src.CompleteDataScienceProject.logger import logging
from src.CompleteDataScienceProject.exception import CustomException
import sys

if __name__ == "__main__":
    ## logging.INFO("YOYOYOYO HONEY SINGH")
    logging.info("YOYOYOYO HONEY SINGH")

    try:
        a= 1/0
    except Exception as e:
        #logging.info("Error Message/ Name - {}".format(e))
        #logging.info("Error Details - {}".format(sys))
        raise CustomException(e,sys)