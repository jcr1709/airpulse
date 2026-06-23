from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args ={
    'owner': 'jc',  
    'retries': 0
}

with DAG(
    dag_id="airpulse_pipeline",
    default_args=default_args,
    description="A simple Airflow DAG to run Airpulse pipeline",
    schedule_interval="@daily",
    start_date=datetime(2026, 6, 23),
    catchup=False,
    tags=["airpulse"],   
) as dag:
    
    run_dbt=BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /opt/airflow/transform && dbt run --profiles-dir . --no-partial-parse',
    )

    test_dbt=BashOperator(
        task_id="test_dbt_models",
        bash_command="cd /opt/airflow/transform && dbt test --profiles-dir . --no-partial-parse",
    )

    run_dbt >> test_dbt
