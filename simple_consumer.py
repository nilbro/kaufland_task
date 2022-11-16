from kafka import KafkaConsumer, KafkaProducer


class Consumer():
    def __init__(self, id) -> None:
        self.c = KafkaConsumer("data-input", bootstrap_servers="localhost:9092", group_id=id)

    def consume_message(self):
        """
        1. Consumes messages from a topic
        2. Sort messages received within a time frame
        """        
        self.local_cache = []

        while True:
            msg_pack = self.c.poll(timeout_ms=50000)
            for tp, messages in msg_pack.items():
                for message in messages:
                    self.local_cache.append(message.value.decode("utf-8"))
            self.local_cache.sort()
            self.send_messages()

    def send_messages(self):
        """
        Sends messages to a topic
        """        
        producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
        for msg in self.local_cache:
            print('Sending messages to output-topic....')
            producer.send("data-output", msg.encode("utf-8"))


if __name__ == "__main__":
    c = Consumer('my-group')
    c.consume_message()
