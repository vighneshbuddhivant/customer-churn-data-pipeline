# Customer Churn Data Analysis Project
This project focuses on analyzing customer churn, which is the process of customers discontinuing their use of a company's services. We used the **Telecom Customer Churn Dataset** (downloaded from Kaggle) and automated an end-to-end ETL pipeline with AWS Glue, Amazon Redshift, and Apache Airflow. We created dashboards for data visualization using **Power BI** and performed SQL queries using **Amazon Athena**.
- **Dataset Source**: [Kaggle - Telecom Customer Churn Dataset](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset?resource=download)
- **YouTube Reference**: [End-to-End Customer Churn Project Walkthrough](https://www.youtube.com/watch?v=VrqO_9MXak0&list=PLACD_PaYcVF1Hzzc1Ds56bD7oUkfiL_Lv&index=11)

## Architecture Overview
![](https://github.com/vighneshbuddhivant/customer-churn-data-pipeline/blob/20c5c625a5ed69ce206e465710ac5219725147b6/customer_churn_pipeline_architecture.png)

1. **Amazon S3**: For storing the customer churn data files.
2. **AWS Glue**: Used for data cataloging and creating ETL jobs.
3. **Amazon Redshift**: Data warehouse for storage and analysis.
4. **Amazon Athena**: For querying the data from the AWS Glue Catalog.
5. **Apache Airflow**: Orchestrates and automates the ETL workflow.
6. **Power BI**: For creating customer churn analysis dashboards.

## Workflow
### 1. AWS Setup
- **Create an IAM User**: Ensure the user has the necessary permissions to interact with S3, Glue, Redshift, and other services.
- **Launch EC2 Instance**: Create an EC2 instance (`ec2_customer_churn_project_instance`) with necessary configurations.

### 2. EC2 Configuration
- **Connect to EC2 Instance** and install required dependencies:
  ```bash
  sudo apt update
  sudo apt install python3-pip
  sudo apt install python3.12-venv
  python3 -m venv customer_churn_youtube_project_venv
  source customer_churn_youtube_project_venv/bin/activate
  ```

- **Install Apache Airflow** in the virtual environment:
  ```bash
  pip install apache-airflow
  pip install apache-airflow-providers-amazon
  airflow standalone
  ```
- **Start Apache Airflow** and ensure port `8080` is open in the security group to access Airflow UI.

### 3. Visual Studio Code Setup
- **Connect Visual Studio Code** to the EC2 instance for better code development using SSH key (refer to [this video](https://www.youtube.com/watch?v=sQQjMnEkGjs) for guidance).

### 4. S3 Bucket & AWS Glue
- **Upload Dataset to S3**: Manually upload the dataset to an S3 bucket (`customer-churn-project-bucket`).
- **Create AWS Glue Crawler**: Create a Glue crawler on the S3 bucket to generate a data catalog. After running the crawler, the table will be created in the AWS Glue catalog.
- **Use Amazon Athena**: Query the dataset using Athena. Store the output in a separate S3 bucket (`customer-churn-athena-result-bucket`).

### 5. Load Data into Amazon Redshift
- **Create Redshift Cluster**: Use Amazon Redshift (we used the serverless version for free usage) and create a database (`dev`).
- **Create Empty Table**: Use SQL to create an empty table in Redshift.
  
- **Glue Connection to Redshift**: 
  1. Create a Glue connection to Redshift.
  2. Create a Glue crawler for the Redshift cluster and run it.

  **Note**: You may encounter errors related to VPC S3 endpoint validation. If so, create an endpoint in the VPC to resolve the issue.

### 6. ETL Job Creation
- **Create AWS Glue ETL Job**: 
  1. Use the Glue visual editor to select the source, perform transformations, and load data into Redshift.
  2. Transform data by removing unnecessary columns, changing column names, and modifying column data types.
  3. Run the ETL job manually first to ensure it's working correctly.

### 7. Automating ETL with Airflow
- **Airflow DAG Creation**:
  1. Write a Python script to create an Airflow DAG.
  2. Store the DAG in `/home/ubuntu/airflow/dags`.
  3. Connect Airflow with AWS using access keys.
  4. Run the Airflow job to automate the ETL process from S3 to Redshift.

### 8. Power BI Dashboard
- **Data Visualization**: After the data is successfully loaded into Redshift, use **Power BI** to create a dashboard that visualizes customer churn data.

## Conclusion
This project demonstrates a complete end-to-end data pipeline from data ingestion to dashboard creation using AWS services. By using Apache Airflow for orchestration, the ETL process is fully automated, making the system scalable and efficient.
