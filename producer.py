#ws://stream.meetup.com/2/rsvps
from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd
import json
import csv
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
value_serializer=lambda x:
dumps(x).encode('utf-8'))
with open('words.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';' , quotechar='|')  
    for row in reader:
        #data = json.dumps(row)
        print(row[0])
        producer.send('streaming_data',value=row[0])
        sleep(1)
        
print("Successfully sent data to kafka topic")