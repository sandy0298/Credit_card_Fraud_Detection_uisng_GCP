import base64
import json
import smtplib
import requests
from google.cloud import secretmanager
from json import loads

def hello_pubsub(event, context):
    # Secret Manager credentials loading
    secret_client = secretmanager.SecretManagerServiceClient()
    project_id = "sandeepdev"
    secret_response = secret_client.access_secret_version(
        {"name": "projects/"+project_id+"/secrets/servicenow/versions/latest"}
    )
    secret_response = secret_response.payload.data.decode("utf-8")
    my_credentials = loads(secret_response)

    # ServiceNow credentials fetched
    servicenow_user = my_credentials["user"]
    servicenow_password = my_credentials["pwd"]

    # SMTP server credentials fetched
    smtp_email = my_credentials["serv_mail"]
    smtp_password = my_credentials["password"]

    # Pub/Sub topic data loading
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    message_json = json.loads(pubsub_message)

    # Write the record to ServiceNow incident table
    url = "https://dev147440.service-now.com/api/now/table/incident"

    # Set credentials for ServiceNow API
    user = servicenow_user
    pwd = servicenow_password

    # Set proper headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Create the incident data
    incident_data = {
        "short_description": "Alert Fraud Transaction Detected",
        "description": f'''
The below transaction has been marked as fraud:

Type: {message_json['type']}
Transaction id: {message_json['id']}
Amount: {message_json['amount']}
Old Balance (Origin): {message_json['oldbalanceOrig']}
New Balance (Origin): {message_json['newbalanceOrig']}
Old Balance (Destination): {message_json['oldbalanceDest']}
New Balance (Destination): {message_json['newbalanceDest']}
Country of Transaction: {message_json['country']}
Receiver's Bank: {message_json['receiver_bank']}
sender_bank :{message_json['sender_bank']}
receiver_name : {message_json['receiver_name']}
time_of_transaction : {message_json['time_of_transaction']}
senders_name : {message_json['senders_name']}
sender's credit card Number : {message_json['nameOrig']}
Receiver's credit card Number : {message_json['nameDest']}
''',
        "urgency": "1",
        "impact": "1",
        "priority": "1",
        "category": "Transaction",
        "subcategory": "Credit Card",
        "caller_id": "gcptest63@gmail.com",
        "assigned_to": "gcpdev3@gmail.com",
    }

    # Do the HTTP request to create the incident
    try:
        response = requests.post(
            url, auth=(user, pwd), headers=headers, json=incident_data
        )
        response.raise_for_status()
        incident_response = response.json()  # Parse the response JSON
        incident_number = incident_response.get("result", {}).get("number")  # Extract the incident number
        print("Incident created successfully. Incident Number:", incident_number)
    except requests.exceptions.RequestException as e:
        print("Error creating incident:", str(e))

    customer_email_pairs = [
    
        {
            "senders_name": "Ethan Thompson","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Olivia Parker","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Noah Anderson","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Ava Mitchell","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Liam Roberts","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Sophia Evans","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Mason Campbell","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Isabella Turner","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Benjamin Hayes","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Mia Collins","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Alexander Reed","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Charlotte Peterson","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "James Murphy","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Amelia Foster","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Samuel Simmons","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Harper Bryant","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Daniel Cox","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Emily Nelson","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Henry Ward","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Scarlett Rivera","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Michael Morgan","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Abigail Hughes","email": "gcptest63@gmail.com"},
        {
            "senders_name": "David Stewart","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Grace Sullivan","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Jackson Price","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Lily Johnson","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Matthew Hayes","email": "sandeep.mohanty1998@gmail.com"},
        {
            "senders_name": "Victoria Gray","email": "gcpdev3@gmail.com"},
        {
            "senders_name": "Samuel Wright","email": "lubumohanty02@gmail.com"},
        {
            "senders_name": "Elizabeth Rogers","email": "gcptest63@gmail.com"},
        {
            "senders_name": "Alex wick","email": "gcptest63@gmail.com"}
    ]


    bank_email_pairs = [
        {"sender_bank": "Bank of America", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "JPMorgan Chase", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "Citibank", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Wells Fargo", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "HSBC", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "Barclays", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "BNP Paribas", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Santander", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Royal Bank of Scotland", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "UBS", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "Deutsche Bank", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Credit Suisse", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Morgan Stanley", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "Bank of China", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "Industrial and Commercial Bank of China (ICBC)", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Bank of Communications", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Standard Chartered Bank", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "Bank of Montreal", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "Toronto-Dominion Bank", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Scotiabank", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Banco Santander", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "BBVA", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "ING Bank", "email": "gcptest63@gmail.com"},
        {"sender_bank": "ABN AMRO", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Societe Generale", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "Crédit Agricole", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "UniCredit", "email": "gcptest63@gmail.com"},
        {"sender_bank": "Intesa Sanpaolo", "email": "lubumohanty02@gmail.com"},
        {"sender_bank": "Nordea Bank", "email": "sandeep.mohanty1998@gmail.com"},
        {"sender_bank": "Danske Bank", "email": "gcpdev3@gmail.com"},
        {"sender_bank": "Union Bank", "email": "gcptest63@gmail.com"}
    ]


    senders_name = message_json["senders_name"]
    sender_bank = message_json["sender_bank"]
    customer_email = ""
    bank_email = ""

    # Find the corresponding email addresses for the customer and bank
    for pair in customer_email_pairs:
        if pair["senders_name"] == senders_name:
            customer_email = pair["email"]
            break

    for pair in bank_email_pairs:
        if pair["sender_bank"] == sender_bank:
            bank_email = pair["email"]
            break

    if not customer_email:
        customer_email = "gcpdev3@gmail.com"
    if not bank_email:
        bank_email = "gcpdev3@gmail.com"

    # Send the email notifications
    email_subject_customer = "Fraud Transaction Detected!!"
    email_body_customer = f'''
Dear {senders_name},

We have detected a fraudulent transaction in your account. Details are as follows:

Type: {message_json['type']}
Transaction id: {message_json['id']}
Amount: {message_json['amount']}
Old Original Balance: {message_json['oldbalanceOrig']}
New Balance : {message_json['newbalanceOrig']}
Country of Transaction: {message_json['country']}
Receiver's Bank: {message_json['receiver_bank']}
sender_bank :{message_json['sender_bank']}
receiver_name : {message_json['receiver_name']}
senders_name : {message_json['senders_name']}
sender's credit card Number : {message_json['nameOrig']}
Receiver's credit card Number : {message_json['nameDest']}

Please contact our customer support (1800 1800) immediately if you have any concerns.

Thank you,
Transaction Admin Team,
TransactionPe Ltd.
'''

    email_subject_bank = "Fraud Transaction Alert - Action Required!!"
    email_body_bank = f'''
Dear Bank Representative,

A fraudulent transaction has been detected from one of your customers. Details are as follows:

Type: {message_json['type']}
Transaction id: {message_json['id']}
Amount: {message_json['amount']}
Old Balance (Origin): {message_json['oldbalanceOrig']}
New Balance (Origin): {message_json['newbalanceOrig']}
Old Balance (Destination): {message_json['oldbalanceDest']}
New Balance (Destination): {message_json['newbalanceDest']}
Country of Transaction: {message_json['country']}
Receiver's Bank: {message_json['receiver_bank']}
sender_bank :{message_json['sender_bank']}
receiver_name : {message_json['receiver_name']}
time_of_transaction : {message_json['time_of_transaction']}
senders_name : {message_json['senders_name']}
sender's credit card Number : {message_json['nameOrig']}
Receiver's credit card Number : {message_json['nameDest']}

An incident ticket {incident_number} has been created for this transaction. Please investigate and help us to take appropriate action.

Thank you,
Transaction Admin Team,
TransactionPe Ltd.
'''

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            email_message_customer = f"Subject: {email_subject_customer}\nFrom: gcpdev3@gmail.com\nTo: {customer_email}\n\n{email_body_customer}"
            email_message_bank = f"Subject: {email_subject_bank}\nFrom: gcpdev3@gmail.com\nTo: {bank_email}\n\n{email_body_bank}"
            server.sendmail(smtp_email, customer_email, email_message_customer)
            server.sendmail(smtp_email, bank_email, email_message_bank)
        print("Emails sent successfully.")
    except Exception as e:
        print("Error sending emails:", str(e))

    print(pubsub_message)
