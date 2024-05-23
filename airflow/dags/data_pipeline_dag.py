from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os


#from scripts.data_collection.scraper import scrape