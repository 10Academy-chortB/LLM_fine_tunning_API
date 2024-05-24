from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
import sys

curent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.dirname(curent_dir)

os.chdir(parent_dir)

sys.path.insert(0, parent_dir)

from scripts.data_collection.scraper import scraper
from scripts.data_processing.clean_text import clean_data

default_args = {
    'owner': 'Group 1',
    'start_date': datetime(2024,5,23),
    'retries': 1
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A data pipeline for scraping, preprocessing and storing data',
    schedule_interval='@daily'
)


scrape_data_task = PythonOperator(
    task_id='scrape',
    python_callable=scraper,
    dag=dag
)



preprocess_data_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=clean_data,
    dag=dag
)

scrape_data_task >> preprocess_data_task