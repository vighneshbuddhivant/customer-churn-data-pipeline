import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1727353288978 = glueContext.create_dynamic_frame.from_catalog(database="customer-churn-s3-glue-database", table_name="customer_churn_project_bucket", transformation_ctx="AmazonS3_node1727353288978")

# Script generated for node Change Schema
ChangeSchema_node1727354112770 = ApplyMapping.apply(frame=AmazonS3_node1727353288978, mappings=[("customerid", "string", "customerid", "string"), ("city", "string", "city", "string"), ("zip code", "long", "zip_code", "int"), ("gender", "string", "gender", "string"), ("senior citizen", "string", "senior_citizen", "string"), ("partner", "string", "partner", "string"), ("dependents", "string", "dependents", "string"), ("tenure months", "long", "tenure_months", "int"), ("phone service", "string", "phone_service", "string"), ("multiple lines", "string", "multiple_lines", "string"), ("internet service", "string", "internet_service", "string"), ("online security", "string", "online_security", "string"), ("online backup", "string", "online_backup", "string"), ("device protection", "string", "device_protection", "string"), ("tech support", "string", "tech_support", "string"), ("streaming tv", "string", "streaming_tv", "string"), ("streaming movies", "string", "streaming_movies", "string"), ("contract", "string", "contract", "string"), ("paperless billing", "string", "paperless_billing", "string"), ("payment method", "string", "payment_method", "string"), ("monthly charges", "double", "monthly_charges", "double"), ("total charges", "double", "total_charges", "double"), ("churn label", "string", "churn_label", "string"), ("churn value", "long", "churn_value", "int"), ("churn score", "long", "churn_score", "int"), ("churn reason", "string", "churn reason", "string")], transformation_ctx="ChangeSchema_node1727354112770")

# Script generated for node Amazon Redshift
AmazonRedshift_node1727354192411 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1727354112770, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://aws-glue-assets-448049823468-ap-south-1/temporary/", "useConnectionProperties": "true", "dbtable": "public.customer_churn", "connectionName": "Redshift_connection", "preactions": "CREATE TABLE IF NOT EXISTS public.customer_churn (customerid VARCHAR, city VARCHAR, zip_code INTEGER, gender VARCHAR, senior_citizen VARCHAR, partner VARCHAR, dependents VARCHAR, tenure_months INTEGER, phone_service VARCHAR, multiple_lines VARCHAR, internet_service VARCHAR, online_security VARCHAR, online_backup VARCHAR, device_protection VARCHAR, tech_support VARCHAR, streaming_tv VARCHAR, streaming_movies VARCHAR, contract VARCHAR, paperless_billing VARCHAR, payment_method VARCHAR, monthly_charges DOUBLE PRECISION, total_charges DOUBLE PRECISION, churn_label VARCHAR, churn_value INTEGER, churn_score INTEGER, churn reason VARCHAR); TRUNCATE TABLE public.customer_churn;"}, transformation_ctx="AmazonRedshift_node1727354192411")

job.commit()