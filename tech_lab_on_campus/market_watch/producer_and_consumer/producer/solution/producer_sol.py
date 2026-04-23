import os
import pika
from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        super().__init__(routing_key, exchange_name)

    def setupRMQConnection(self) -> None:
        url = os.environ.get('AMQP_URL', 'amqp://localhost')
        self.connection = pika.BlockingConnection(pika.URLParameters(url))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')