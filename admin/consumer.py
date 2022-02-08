import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product
import pika, json

params = pika.URLParameters('amqps://uaxlnedb:9UCuihjfOv7MZkMr1K14vJ15PndqKMeQ@vulture.rmq.cloudamqp.com/uaxlnedb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    id = json.loads(body)
    product = Product.objects.get(id = id)
    product.likes = product.likes + 1
    product.save()
    print ('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()


