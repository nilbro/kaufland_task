# kaufland_task

## Reproducible Environment

### Requirements
1. One topic ``data-input`` with 10 partitions
2. (Sample) data to be sent to individual partitions in ascending order --> need some external api for that
3. Number of messages can exceed the amount of memory available on the
machine --> proper log retention policy needed
4. Docker-based development environment 

### Setup the environment
```bash
$ docker-compose up -d
```
Check messages per partition in the topic
```
$ docker exec --interactive --tty broker \
    kafka-console-consumer \ 
    --bootstrap-server broker:9092 \
    --topic data-input \
    --formatter kafka.tools.DefaultMessageFormatter \
    --property print.partition=true \
    --from-beginning
```
## Simple Consumer

### Requirements
1. One topic ``data-output`` on the consumer side with just 1 partition.
2. An application which reads messages from the ``data-input`` topic and publishes them to ``data-output`` with increasing order.

### Observations and Assumptions 

Since there is a need for maintining order, we need to compare between the messages from different partitions. Hence there is a need to maintain the state. 

#### Assumption 1
If the messages in ``data-input`` topic do not have an end, the application will order the messages over a time window before publishing to the ``data-output`` topic.

#### Assumption 2
If the messages in ``data-input`` topic do have an end, the application will order the messages that it has received before publishing to the ``data-output`` topic.

### Assumption 3
The application will order the messages that it has received in a time-window before publishing to the ``data-output`` topic.

The third assimption is considered here.

### Run the consumer

```bash
$ python simple_consumer.py
```

In another terminal, check the ``data-output`` topic

```bash
$ docker exec --interactive --tty broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic data-output \
                       --formatter kafka.tools.DefaultMessageFormatter \
                       --property print.partition=true 
```

Start pushing sample data in ``data-input`` topic

```bash
$ docker-compose up -d
```

## Scalable Consumer

### Requirements

1. The consumer should be scalable. Multiple workers should work concurrently.
2. Each partition should be consumed exactly one worker.

To meet the requirements, a consumer group with 10 consumers (= number of partitions) should be used.