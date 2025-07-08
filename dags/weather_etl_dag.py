from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow')

from etl.extract import extract
from etl.transform import transform
from etl.load import load

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    description="ETL pipeline for weather data"
) as dag:

    task1 = PythonOperator(
        task_id="extract_weather",
        python_callable=extract
    )

    task2 = PythonOperator(
        task_id="transform_weather",
        python_callable=transform
    )

    task3 = PythonOperator(
        task_id="load_weather",
        python_callable=load
    )

    task1 >> task2 >> task3