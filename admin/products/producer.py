import pika

params = pika.URLParameters('amqps://uaxlnedb:9UCuihjfOv7MZkMr1K14vJ15PndqKMeQ@vulture.rmq.cloudamqp.com/uaxlnedb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')