zkServer

Inicializar servidor
    .\bin\windows\kafka-server-start config\server.properties

Criar topico
    .\bin\windows\kafka-topics.bat --create --zookeeper localhost:9092 --replication-factor 1 --partitions 1 --topic test
    .\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic streaming_data

Producer
    .\bin\windows\kafka-console-producer --broker-list localhost:9092 --topic streaming_data

Consumer
    .\bin\windows\kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming_data --from-beginning


List Kafka
    bin/windows/kafka-topics --list --zookeeper localhost:2181



#os.environ['PYSPARK_SUBMIT_ARGS'] = ' — packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.1.0,org.apache.spark:spark-sql-kafka-0–10_2.11:2.1.0 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = ' — packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.3.0 pyspark-shell'