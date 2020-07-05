#python2 -m pip install  pyspark==2.2.1
from pyspark import SparkConf, SparkContext
from operator import add
import sys
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def handler(message):
    records = message.collect()
    for record in records:
        producer.send('', str(record))
        producer.flush()

def main():
    sc = SparkContext(appName="PythonStreamingDirectKafkaWordCount")
    ssc = StreamingContext(sc, 10)

    brokers, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    kvs.foreachRDD(handler)

    ssc.start()
    ssc.awaitTermination()
if __name__ == "__main__":

   main()
   
   
   
   

-------------------------------------------------

from pyspark.streaming.kafka import KafkaUtils
import sys
import os 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json


os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.10:2.0.2 pyspark-shell'  

sc = SparkContext("local[2]", "KafkaSTREAMWordCount")
ssc = StreamingContext(sc, 2)
kafka_stream = KafkaUtils.createStream(ssc,"localhost:2181","raw-event-streaming-consumer",{"streaming_data":1})

parsed = kafka_stream.map(lambda k, v: json.loads(v))
parsed.pprint()
ssc.start()
ssc.awaitTermination()