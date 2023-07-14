import csv
import time
import json
from google.cloud import pubsub_v1
project_id = 'sandeepdev'
topic_name = 'credit_transaction'
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id,topic_name)
filename = '/home/sandeepdev751/fraud_data.csv'
time_delay = 10
with open(filename, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Convert the row to JSON or any desired format
        data = {
            'type': row['type'],
            'id': row['id'],
            'amount': row['amount'],
            'oldbalanceOrig': float(row['oldbalanceOrig']),
            'newbalanceOrig': float(row['newbalanceOrig']),
            'oldbalanceDest': float(row['oldbalanceDest']),
            'newbalanceDest': float(row['newbalanceDest']),
            'country': row['country'],
            'senders_name':row['senders_name'],
            'receiver_bank':row['receiver_bank'],
            'sender_bank':row['sender_bank'],
            'receiver_name':row['receiver_name'],
            'time_of_transaction':row['time_of_transaction'],
            'nameOrig':row['nameOrig'],
            'nameDest':row['nameDest']
        }

        message_data = json.dumps(data).encode('utf-8')
                
        # Publish the data to the Pub/Sub topic
        publisher.publish(topic_path, data=message_data)
        print("Published record:", data)

        # Introduce time delay
        time.sleep(time_delay)
        
