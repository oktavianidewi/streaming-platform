# [Day-1] Introduction to Kafka

## Event, streaming, pub/sub

### What is an Event

### What is Stream Processing

### What is pub/sub system? 
- how does it different with queues?

### What is Redpanda?

- how to see topic in redpanda


### Publisher

### Consumer

## Concept of Topic, Partitions and Offset

- https://www.geeksforgeeks.org/topics-partitions-and-offsets-in-apache-kafka/

- https://www.geeksforgeeks.org/how-kafka-producers-message-keys-message-format-and-serializers-work-in-apache-kafka/

- https://www.geeksforgeeks.org/how-kafka-consumer-and-deserializers-work-in-apache-kafka/


```
python -m venv .venv
source .venv/bin/activate
pip install confluent_kafka
```

## Implementation of Streaming Data Ingestion without Schema

### Spin up docker

```
docker-compose -f kafka/docker-compose.yml up
```

- if the port is conflict, change the host port to `8085`

```
    ports:
      - 8085:8080
```

- access redpanda via browser

![](./img/streaming__redpd_dashboard.png)


[ASK: perlu gak ya?]
## Improvement on Streaming Data Ingestion Using Avro Schema

Records in a topic are just arrays of bytes. Kafka broker doesn’t care about the type of data we’re sending. To make those byte arrays useful in our applications, producers and consumers must know how to interpret them.

- https://codingharbour.com/apache-kafka/why-use-avro-data-format-with-apache-kafka
- https://towardsdatascience.com/using-kafka-with-avro-in-python-da85b3e0f966
- https://levelup.gitconnected.com/kafka-schema-registry-b5eb8afac228

### Avro Schema

- what is avro schema : https://www.tutorialspoint.com/avro/avro_schemas.htm

- Define avro schema for our streaming data [here](./kafka/avro/schema/stocks_schema.avsc)

```

```




## [TASK] Create topic, publisher and consumer

# [Day-4] Streaming Data with Apache Spark

## What is Apache Spark? 

Why do we need Spark, instead of Python?

Distributed system

## Spin up Apache Spark and Redpanda with docker 



### 1. Build Required Images for running Spark
The details of how to spark-images are build in different layers can be created can be read through the blog post written by André Perez on Medium blog -Towards Data Science

###  Build Spark Images

```
chmod 755 build.sh
sh build.sh
```

https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_6_stream_processing/python/docker/README.md


#### 3. Run Services on Docker
Start Docker-Compose (within for kafka and spark folders)

```
docker compose up -d
```

In depth explanation of Kafka Listeners

Explanation of Kafka Listeners

### 4. Stop Services on Docker
Stop Docker-Compose (within for kafka and spark folders)

``` docker compose down ```



## Read from kafka topic with PySpark

https://redpanda.com/blog/buildling-streaming-application-docker-spark-redpanda 

```

### Running Producer and Consumer

- Run producer

```
python3 producer.py
```

- Run consumer with default settings

```
python3 consumer.py
```

- Run consumer for specific topic

```
python3 consumer.py --topic <topic-name>

```

- Running Streaming Script

spark-submit script ensures installation of necessary jars before running the streaming.py

```
./spark-submit.sh streaming.py 
```


compatibility spark in cloud: 
- AWS: Glue
- GCP: Dataproc