# code adapted from https://medium.com/data-hackers/primeiros-passos-com-o-apache-airflow-etl-fácil-robusto-e-de-baixo-custo-f80db989edae

from airflow import example_dags
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'marcos_teixeira',
    'depends_on_past': False,
    'start_date': datetime(2021,5,13),
    'retries': 0,
}

# naming the DAG and schedules
with DAG(
    'initial-dag',
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    default_args=default_args
) as dag:

    # task definitions
    task1 = BashOperator(
        task_id='first_etl',
        bash_command="""
        cd /Users/marcostexeira/airflow/dags/etl_scripts/
        python3.8 first_etl.py
        """
    )

    task2 = BashOperator(
        task_id='second_etl',
        bash_command="""
        cd /Users/marcostexeira/airflow/dags/etl_scripts/
        python3.8 second_etl.py
        """
    )

# execution order

task1 >> task2