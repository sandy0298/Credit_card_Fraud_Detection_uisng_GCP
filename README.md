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

<img src = "https://github.com/sandy0298/Credit_card_Fraud_Detection_uisng_GCP/blob/main/screenshots/Screenshot%20(8).png" width="800" height="600" alt="report1"/> &emsp;
<img src ="https://github.com/sandy0298/Credit_card_Fraud_Detection_uisng_GCP/blob/main/screenshots/Screenshot%20(9).png" width="800" height="600" alt="report2"/> &emsp;
<img src ="https://github.com/sandy0298/Credit_card_Fraud_Detection_uisng_GCP/blob/main/screenshots/Screenshot%20(10).png" width="800" height="600" alt="report2"/> &emsp;

## Link to Dashboard

## Fraud data dashboard
https://lookerstudio.google.com/reporting/0c7642cd-4159-4fb6-a601-ef2c2ebb37dd

## Non-Fraud Data Dashboard
https://lookerstudio.google.com/reporting/0bd09fe9-0f04-4acb-a8f5-617ad1d4c80b

### Code structure
```
├── Home Directory
|     ├── transaction_pubsub.py
|     ├── Datastreaming_ingestion.py
├── setup.py
 
```
## Installation Steps and deployment process

## 1. Run the streaming dataflow Pipeline (datastream_ingestion.py):
   a. Start the dataflow_ingestion.py script, which initiates the streaming dataflow pipeline.
   b. The pipeline is designed to continuously pull data from a pub/sub subscriber.
   c. The pulled data is then stored in Firestore, a NoSQL document database.
   d. Within the pipeline, various operations can be performed on the data, including predictions using machine learning models or any other required transformations.

## 2. Load transaction records to pub/sub (transaction_pubsub.py):
   a. Execute the transaction_pubsub.py script to load transaction records into a pub/sub topic.
   b. This script ensures that new transaction records are continuously published to the specified pub/sub topic in real-time.
   c. These records will be processed by downstream components, such as the streaming dataflow pipeline.

## 3. Trigger cloud function on fraud record from pub/sub:
   a. Deploy a cloud function that is designed to trigger when a fraud record is detected within the pub/sub topic.
   b. Configure the cloud function to listen to the specific pub/sub topic where the fraud records are published.
   c. When a new fraud record is detected, the cloud function is triggered automatically.
   d. The cloud function can then execute custom logic, such as sending email notifications or creating ServiceNow tickets based on the detected fraud.

## 4. Create email notifications and ServiceNow tickets:
   a. Within the cloud function triggered by the fraud record, include the necessary code to send email notifications.
   b. Utilize appropriate email sending APIs or services to compose and send the notifications to relevant stakeholders.
   c. Similarly, within the cloud function, integrate with the ServiceNow API to create new tickets based on the fraud record.
   d. Provide the required details and fields to create a new ticket with relevant information about the fraud incident.
   e. Ensure proper error handling and logging mechanisms are in place to track the status and outcomes of the email notifications and ServiceNow ticket creation.

These steps outline the process of deploying and running the necessary components to handle the streaming dataflow pipeline, pub/sub integration, fraud detection triggering, and subsequent email notifications and ServiceNow ticket creation.


