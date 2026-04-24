from consumer_interface import mqConsumerInterface
import pika

class mqConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name

        self.setupRMQConnection()


    def consume(self) -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOST", "localhost:15672/")))
        channel = connection.channel()
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message_callback, auto_ack=True)
        channel.start_consuming()

    