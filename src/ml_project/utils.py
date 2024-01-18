import os 
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import  custom_exception
import pandas as pd 
from dotenv import load_dotenv      # used to load environment variables from a file named .env

#Load environment variables from .env file
load_dotenv()

# Access the environment variables

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_data():
    logging.info("reading the data")
     
    try:
       