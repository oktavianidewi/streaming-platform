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