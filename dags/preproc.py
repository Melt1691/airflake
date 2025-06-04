from airflow import DAG 
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator # Allows us to transfer files from local filesystem to S3
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor # Asynchronouly detects files in S3 then uploads it
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # To run a Databricks notebook
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator # To run Snowflake operations
from airflow.providers.amazon.aws.hooks.s3 import S3Hook # To interact with S3 bucket, pull/move data inside S3.
from datetime import datetime, timedelta # To use solid date and time objects
import json # Handle API requests that pull data 

S3_BUCKET = "my-airflow-bucket"
RAW_S3_KEY = "raw_data/data.json"
PROCESSED_S3_KEY = "processed_data/"
DATABRICKS_JOB_ID = "1234567890"

# Snowflake configuration
SNOWFLAKE_CONN_ID = "my_snowflake_conn"
SNOWFLAKE_RAW_TABLE = "RAW_TABLE"
SNOWFLAKE_PROCESSED_TABLE = "MODEL_RESULTS"
SNOWFLAKE_SCHEMA = "PUBLIC"
SNOWFLAKE_DATABASE = "MY_DB"

# Databricks Configuration
DATABRICKS_CONN_ID = "databricks_default"