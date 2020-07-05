from kafka import KafkaProducer
import json,time
userdata={
        "ipaddress": "172.16.0.57",
        "logtype": "",
        "mid": "",
        "name":"TJ"
}
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(10):
    print("adding",i)
    producer.send('streaming_data', userdata)
    time.sleep(3)