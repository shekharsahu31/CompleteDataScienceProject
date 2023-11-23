import os
import sys
from src.CompleteDataScienceProject.exception import CustomException
from src.CompleteDataScienceProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")
port = int(os.getenv("port"))

print(host,user,password,db,port)

'''host = "127.0.0.1"
user = "root"
password = "shekhar"
db = "college"
port = 3306'''


def read_sql_data():
    logging.info("Reading MYSQL Database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=port )
        
        logging.info(f"Connection Established {mydb}")
        df=pd.read_sql_query('select * from student' , mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)
    
def save_pickle_object(path , obj):
    try:
        dir_path = os.path.dirname(path)

        os.makedirs(dir_path, exist_ok = True)
        
        with open(path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
