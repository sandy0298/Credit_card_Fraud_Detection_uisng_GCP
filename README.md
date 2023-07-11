# Credit Card Fraud Detection Using GCP
This project aims to develop a comprehensive credit card fraud transaction detection system for Global Bank Limited. The system leverages historical financial and demographic data to train a machine learning model using BigQuery Machine Learning (BQML). The trained model is deployed on Vertex AI Endpoint, enabling real-time fraud prediction on incoming credit card transactions. The project also incorporates data streaming, storage, incident handling, and reporting components to provide a holistic solution for fraud detection and prevention.

## Toolbox 🧰
<img src="https://miro.medium.com/v2/resize:fit:335/0*ARUQelkPpC1LwNFN" width="200" height="120" alt="Pub Sub"/> &emsp; <img src="https://lh6.googleusercontent.com/1MICxjbrbRPtEnzE54g2shaMRD2RocCIcuSOrqwaqryObCR6IrsXNb3Sd5MjBBwmoLeVcgVu_SE3vw-IbRA24SFhH4IT1xppVuuNGodDtFEykgD0Cw1vB2jITTsOgBNHvWfw27icmMs30SYgWQ" width="200" alt="GCP DTAFLOW" height="70"/>
&emsp; <img src="https://miro.medium.com/max/600/1*HEzofakm1-c4c_Qn4zjmnQ.jpeg" width ="170" height="75" alt="Apache Beam"/>
&emsp;<img src ="https://i.ytimg.com/vi/s6ytxB0YSR0/mqdefault.jpg" width="170" height="70" alt="Secret Manager"/> &emsp;
<img src ="https://th.bing.com/th/id/OIP.k11NKB6vQbDyHstjaXOJygHaCk?pid=ImgDet&rs=1" width="200" height="100" alt="Google Cloud Storage"/> &emsp;
<img src ="https://cxl.com/wp-content/uploads/2019/10/google-bigquery-logo-1.png" width="170" height="100" alt="Google Big Query"/> &emsp;
<img src ="https://miro.medium.com/v2/resize:fit:584/1*q4EVSAndlvgFLyR6ncc4Bg.png" width="170" height="100" alt="Google cloud Functions"/> &emsp;
<img src ="https://assets.website-files.com/618399cd49d125734c8dec95/63905b4ecedc3f60172bcd63_vertexai.png" width="170" height="100" alt="Vertex AI"/> &emsp;
<img src ="https://res.cloudinary.com/hevo/image/upload/f_auto,q_auto/v1685918308/hevo-learn-1/Firestore-Data-Model-firestore-logo.png?_i=AA" width="170" height="100" alt="Google cloud Firestore"/> &emsp;
<img src ="https://miro.medium.com/v2/resize:fit:961/1*tQKERQdZsjUArxXjaHo9PA.png" width="170" height="100" alt="Secret Manager"/> &emsp;
<img src ="https://logos-world.net/wp-content/uploads/2022/02/ServiceNow-Symbol.png" width="100" height="100" alt="ServiceNow"/> &emsp;
<img src ="https://i.pinimg.com/originals/8d/39/f3/8d39f3958e82028615cdedacb496a114.jpg" width="170" height="100" alt="SMTP"/> &emsp;
<img src ="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" width="170" height="100" alt="Python"/> &emsp;

## Architecture Diagram

<img src ="https://github.com/sandy0298/Credit_card_Fraud_Detection_uisng_GCP/blob/main/screenshots/credit_card_architecture.png" width="900" height="700" alt="architecture"/> &emsp;

## Project Workflow:

## 1. Data Training:
   - Historical financial and demographic data is collected and stored in BigQuery.
   - **BQML** is used to preprocess and analyze the data, training a credit card fraud transaction model.
   - The model is optimized to identify patterns and features indicative of fraudulent transactions.

## 2. Model Deployment:
   - The trained model is deployed on **Vertex AI** Endpoint, which offers a scalable and robust infrastructure for hosting and serving machine learning models.
   - The endpoint provides a REST API for real-time prediction on new credit card transactions.

## 3. Real-Time Transaction Processing:
   - Incoming credit card transactions from on-prem servers are streamed to a Pub/Sub topic.
   - A streaming Dataflow pipeline is implemented to consume and process each transaction record from the Pub/Sub subscriber.
   - The pipeline performs data transformation, validation, and enrichment tasks before loading the records into a **Firestore** database for further analysis.

## 4. Fraud Prediction:
   - The Dataflow pipeline forwards each transaction record to the deployed Vertex AI Endpoint.
   - The endpoint applies the trained model to predict the likelihood of fraud for each transaction.
   - The endpoint returns a result in the form of a binary classification label, represented by an "**is_fraud**" column in the output.

## 5. Data Storage:
   - Based on the predicted fraud label, the transaction records are stored in BigQuery tables for further analysis and reporting.
   - Transactions labeled as non-fraudulent (**is_fraud = 0**) are written to the "non_fraud_transaction" table.
   - Transactions labeled as fraudulent (**is_fraud = 1**) are written to the "fraud_transaction_layer" table.

## 6. Fraud Alert and Incident Handling:
   - For transactions flagged as fraudulent (is_fraud = 1), a record is published to another Pub/Sub topic specifically for fraud alerts.
   - A **cloud function** is triggered by the published record, responsible for **sending email notifications** to the customers associated with the fraudulent transactions.
   - Additionally, the cloud function creates **high-priority incident tickets in ServiceNow**, the bank's incident management system.
   - The cloud function securely retrieves the required credentials from Secret Manager to access the necessary resources for sending emails and creating incident tickets.

## 7. Reporting and Visualization:

   - **Looker** Dashboards are developed to provide comprehensive visualizations and insights into both fraud and non-fraud transactions.
   - The dashboards include interactive charts, graphs, and metrics to help stakeholders monitor transaction patterns, detect potential fraud trends, and make data-driven decisions.
   - Key performance indicators, such as fraud detection rates and transaction volumes, are visualized to provide a comprehensive overview of the system's effectiveness.

## Conclusion:

This GitHub project demonstrates a sophisticated credit card fraud transaction detection system implemented for Global Bank Limited. The solution combines data training using BQML, model deployment on Vertex AI Endpoint, real-time transaction processing with Dataflow and Pub/Sub, data storage in BigQuery, fraud alerting and incident handling with cloud functions and ServiceNow integration, and reporting and visualization through Looker Dashboards. By utilizing these technologies, the project offers a scalable, automated, and comprehensive solution for credit card fraud detection, enabling Global Bank Limited to mitigate risks, protect its customers, and enhance overall security.

## Dashboard

<img src = "https://github.com/sandy0298/Aviation_real_time_streaming/blob/main/images/report1.jpg" width="800" height="600" alt="report1"/> &emsp;
<img src ="https://github.com/sandy0298/Aviation_real_time_streaming/blob/main/images/report2.jpg" width="800" height="600" alt="report2"/> &emsp;

## Link to Dashboard

https://lookerstudio.google.com/s/nB_GDX1CYq8



### Code structure
```
├── Home Directory
|     ├── pubsub_aviation.py
|     ├── Datastreaming_ingestion.py

 
```
## Installation Steps and deployment process
<b>1.</b>For running Dataflow We need to install Java Jdk 8 on the master node. For that we are making use of GCS Bucket to hold the JDk 8 Package and installing the dependency at run time on the master Node.<br>
<b>2.</b>first we need to run our Dataflow Pipeline script i.e datastreaming.py which will build the streaming pipeline for data ingestion activity to bigquery with a fixed window session of 50 seconds i.e data from the pubsub will be pulled to dataflow and will be ingested to bigquery in realtime. <br>
<b>3.</b> Then we need to run the pubsub_aviation.py script as it will publish the json Paylod from aviation API to the Pub/Sub topic. we have defined a sleep timer of 10 seconds in the code.<br>
<b>4.</b>For security purpose we are making use of Gcp Secret Manager to hold the Aviation Access API and are fetching them at run time.<br>
<b>5.</b>We are holding the Schema of Big Query Tables in our dataflow pipeline code.<br>
<b>6.</b> Data from Bigquery is ingested to looker studio and insights are generated with some KPIs. <br>


