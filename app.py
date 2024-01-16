from src.ml_project.logger import logging
from src.ml_project.exception import  custom_exception
import sys
if __name__ == "__main__":
    logging.info("started")


    try:
        a = 1/0

    except Exception as e :
       logging.info("EXCEPTION")
       raise  custom_exception(e,sys)