# KSQL

With KSQL, you can access kafka topic using SQL.

```bash
docker exec -it  ksqldb-cli bash
```

Then run the following:

```bash
ksql http://ksqldb-server:8088
```

Create stream, notice that we need to to create a structure that match or kafka topic value.

```sql
CREATE STREAM sample_table_stream (
    payload STRUCT<
        before STRUCT<
            id INT,
            name VARCHAR(100),
            age INT,
            created_at BIGINT
        >,
        after STRUCT<
            id INT,
            name VARCHAR(100),
            age INT,
            created_at BIGINT
        >
    >
) WITH (
    KAFKA_TOPIC = 'postgres.public.sample_table',
    VALUE_FORMAT = 'JSON'
);
```

Try to show all data.

```sql
SELECT payload->after->id, payload->after->name, payload->after->age, payload->after->created_at
FROM sample_table_stream 
```

Or only the latest changes

```sql
SELECT payload->after->id, payload->after->name, payload->after->age, payload->after->created_at
FROM sample_table_stream 
EMIT CHANGES;
```

![](img/ksql-insert.png)