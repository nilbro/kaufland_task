from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient


def simple_consumer():
    c = KafkaConsumer("data-input", bootstrap_servers="localhost:9092")

    local_cache = []

    while True:
        msg_pack = c.poll(timeout_ms=50000)
        for messages in msg_pack.items():
            for message in messages:
                print(message.value.decode('utf-8'))
                local_cache.append(message.value.decode('utf-8'))
        local_cache.sort()
        send_messages(local_cache)


def send_messages(sorted_list: list):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    for msg in sorted_list:
        producer.send('data-output', msg.encode("utf-8"))


if __name__ == "__main__":
    simple_consumer()

