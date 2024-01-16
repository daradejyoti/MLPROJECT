import logging
import os 

from datetime import datetime

# create a log file based on date and time

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Retrieves the current working directory using os.getcwd()
current_directory= os.getcwd()

 # Create a path for the log file inside a 'logs' directory in the current working directory
log_path = os.path.join(current_directory,log_file)

# Ensure that the directory structure exists, and if not, create it
os.makedirs( log_path, exist_ok= True)

#Create the full path for the log file
log_file_path =os.path.join(log_path,log_file) 

logging.basicConfig(
    filename=log_file_path,
    format= '[%(asctime)s] %(lineno)d %(name)s -%(levelname)s- %(message)s',
    level= logging.INFO
)