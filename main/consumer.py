import pika

params = pika.URLParameters('amqps://uaxlnedb:9UCuihjfOv7MZkMr1K14vJ15PndqKMeQ@vulture.rmq.cloudamqp.com/uaxlnedb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()

