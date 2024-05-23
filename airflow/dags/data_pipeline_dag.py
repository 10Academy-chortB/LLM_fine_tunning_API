from airflow import dag
from airflow.operators.python_operators import PythonOperator
from datetime import datetime
import os


#from scripts.data_collection.scraper import scrape