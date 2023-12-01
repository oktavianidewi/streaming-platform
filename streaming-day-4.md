# [Day-4] Streaming Data with Apache Spark

## What is Apache Spark? 

Apache Spark is a data processing framework that can quickly perform processing tasks on very large data sets, and can also distribute data processing tasks across a distributed system.  It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs.

PySpark is a high-level API that is provided by Apache Spark. PySpark can be used to perform common data analysis tasks, such as filtering, aggregation, and transformation of large datasets on a distributed system.

In the previous material, we learned Pandas to transform the dataset. So, what makes PySpark different from Pandas? 

There is a difference in their execution and processing architecture. 

## Install PySpark locally

You should either use the spark-submit command to run the PySpark (Spark with python) application or use the PySpark shell to run interactive commands for testing.

Note: Do not use Python shell or Python command to run PySpark program.

read from kafka:
- https://subhamkharwal.medium.com/pyspark-structured-streaming-read-from-kafka-64c40767155f


## Spin up Apache Spark and Redpanda with docker 

```
docker-compose -f docker/spark/docker-compose.yml up
```


https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_6_stream_processing/python/docker/README.md


why "--packages"

https://stackoverflow.com/questions/48011941/why-does-formatkafka-fail-with-failed-to-find-data-source-kafka-even-wi


#### to not use docker 

#### to use docker 


### 4. Stop Services on Docker
Stop Docker-Compose (within for kafka and spark folders)

``` docker compose down ```

The web UI ports are published to localhost for  the Spark master (8080) and Spark worker (8081)


## Read from kafka topic with PySpark

https://redpanda.com/blog/buildling-streaming-application-docker-spark-redpanda 


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

# Resources:
- https://medium.com/geekculture/pandas-vs-pyspark-fe110c266e5c