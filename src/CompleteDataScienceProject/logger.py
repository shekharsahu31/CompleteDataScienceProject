import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ### Creates Folder + File of this Name under logs folder 
                                                               ### thats why LOG_File is used twice below
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

###### CREATING OUR OWN CUSTOM LOGGING FUNCTOIN TO PUT EACH LOGS IN A FILE WITH SPECIFIC DATE AND TIME AND ETC FORMATS #######