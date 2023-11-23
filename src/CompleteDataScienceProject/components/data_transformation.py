import sys 
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.CompleteDataScienceProject.exception import CustomException
from src.CompleteDataScienceProject.logger import logging
from src.CompleteDataScienceProject.utils import save_pickle_object
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self,X):
        '''
        this function is responsible for transformation
        '''
        try:
            "math_score"

            '''num_features = ["writing_score", "reading_score"]
            cat_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]'''

            # Create Column Transformer with 3 types of transformers
            X = X.drop(columns=['math_score'], axis=1)
            num_features = X.select_dtypes(exclude="object").columns
            cat_features = X.select_dtypes(include="object").columns

            '''numeric_transformer = StandardScaler()
            oh_transformer = OneHotEncoder()

            preprocessor = ColumnTransformer(
                [
                    ("OneHotEncoder", oh_transformer, cat_features),
                    ("StandardScaler", numeric_transformer, num_features),        
                ]
            )'''

            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler())

            ])
            cat_pipeline=Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("one_hot_encoder",OneHotEncoder()),
            ("scaler",StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical Columns: {cat_features}")
            logging.info(f"Numerical Features : {num_features}")


            preprocessor = ColumnTransformer(
                [
                    ("NumTransf", num_pipeline, num_features),
                    ("CatTransf", cat_pipeline, cat_features),        
                ]
            )

            return preprocessor
        

        except Exception as e:
            raise CustomException(e,sys)



    def initiate_data_transformation(self,raw_path, train_path, test_path):
        try:
            df = pd.read_csv(raw_path)
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Reading the train and test file")

            preprocessorobj = self.get_data_transformer_object(df)
            #traget_variable= 'math_score'
            train_df_without_target = train_df.drop(columns=['math_score'], axis=1)
            train_target = train_df['math_score']
            test_df_without_target = test_df.drop(columns=['math_score'], axis=1)
            test_target = test_df['math_score']

            logging.info("Applying PreProcessing Techq.")

            train_df_arr = preprocessorobj.fit_transform(train_df_without_target)
            test_df_arr = preprocessorobj.transform(test_df_without_target)
            
            train_arr = np.c_[
                train_df_arr + np.array(train_target).reshape(-1,1)]
            
            test_arr = np.c_[
                test_df_arr + np.array(test_target).reshape(-1,1)]
            
            save_pickle_object(path=self.data_transformation_config.preprocessor_obj_file_path,
                               obj = preprocessorobj)
              
            logging.info("Saving Pickle File")

            return (train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path)    


        except Exception as e:
            raise CustomException(e,sys)







