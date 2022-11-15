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

