from airflow import DAG
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

ssh_hook = SSHHook(ssh_conn_id='local_ssh')

with DAG('data_process_layers', default_args=default_args, schedule_interval=None) as dag:

    run_banks_raw = SSHOperator(
        task_id='run_banks_raw',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/1_Raw/banks_raw.py', 
        dag=dag
    )

    run_complaints_raw = SSHOperator(
        task_id='run_complaints_raw',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/1_Raw/complaints_raw.py', 
        dag=dag
    )

    run_employees_raw = SSHOperator(
        task_id='run_employees_raw',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/1_Raw/employees_raw.py', 
        dag=dag
    )

    run_banks_trusted = SSHOperator(
        task_id='run_banks_trusted',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/2_Trusted/banks_trusted.py', 
        dag=dag
    )

    run_complaints_trusted = SSHOperator(
        task_id='run_complaints_trusted',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/2_Trusted/complaints_trusted.py', 
        dag=dag
    )

    run_employees_trusted = SSHOperator(
        task_id='run_employees_trusted',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/2_Trusted/employees_trusted.py', 
        dag=dag
    )

    run_reviews_complaints_delivery_parquet = SSHOperator(
        task_id='run_reviews_complaints_delivery_parquet',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/3_Delivery/reviews_complaints_delivery_parquet.py', 
        dag=dag
    )

    run_reviews_complaints_delivery_validation = SSHOperator(
        task_id='run_reviews_complaints_delivery_validation',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/3_Delivery/reviews_complaints_delivery_validation.py', 
        dag=dag
    )

    run_reviews_complaints_delivery_db = SSHOperator(
        task_id='run_reviews_complaints_delivery_db',
        ssh_conn_id='local_ssh',
        command='source /home/alves/.venv/bin/activate && python /home/alves/Projetos/eEDB-011-2024-3/atividade_3/scripts/3_Delivery/reviews_complaints_delivery_db.py', 
        dag=dag
    )

    run_banks_raw >> run_complaints_raw >> run_employees_raw >> run_banks_trusted >> run_complaints_trusted >> run_employees_trusted >> run_reviews_complaints_delivery_parquet >> run_reviews_complaints_delivery_validation >> run_reviews_complaints_delivery_db
