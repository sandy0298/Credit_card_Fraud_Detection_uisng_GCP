# Credit_card_Fraud_Detection_uisng_GCP
This Project is about predicting fraud transactions in real time and then doing multiple operations like sending fraud email alerts to customers, creating tickets in servicenow aand finally creating Dashboards for fraud nd non-frua Transactions.

## Toolbox 🧰
<img src="https://image.slidesharecdn.com/googlepresents-iotatgooglescale-slideshare-150827115054-lva1-app6892/95/iot-at-google-scale-9-638.jpg?cb=1440676398" width="200" height="80" alt="Pub Sub"/> &emsp; <img src="https://lh6.googleusercontent.com/1MICxjbrbRPtEnzE54g2shaMRD2RocCIcuSOrqwaqryObCR6IrsXNb3Sd5MjBBwmoLeVcgVu_SE3vw-IbRA24SFhH4IT1xppVuuNGodDtFEykgD0Cw1vB2jITTsOgBNHvWfw27icmMs30SYgWQ" width="200" alt="GCP DTAFLOW" height="70"/>
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



## Dashboard

<img src = "https://github.com/sandy0298/Aviation_real_time_streaming/blob/main/images/report1.jpg" width="800" height="600" alt="report1"/> &emsp;
<img src ="https://github.com/sandy0298/Aviation_real_time_streaming/blob/main/images/report2.jpg" width="800" height="600" alt="report2"/> &emsp;

## Link to Dashboard

https://lookerstudio.google.com/s/nB_GDX1CYq8

## Architecture Diagram

<img src ="https://github.com/sandy0298/Aviation_real_time_streaming/blob/main/aviation_data_final.png" width="800" height="600" alt="architecture"/> &emsp;

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


