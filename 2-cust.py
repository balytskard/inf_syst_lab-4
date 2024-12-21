import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='stock_exchange', exchange_type='direct')


companies = ['apple', 'google', 'amazon']

def callback(ch, method, properties, body):
    print(f"Отримано повідомлення з ключем {method.routing_key}: {body.decode()}")

for company in companies:
    channel.queue_declare(queue=f'{company}_queue')
    channel.queue_bind(exchange='stock_exchange', queue=f'{company}_queue', routing_key=f'stock.{company}.buy')
    channel.queue_bind(exchange='stock_exchange', queue=f'{company}_queue', routing_key=f'stock.{company}.sell')
    channel.basic_consume(queue=f'{company}_queue', on_message_callback=callback, auto_ack=True)

print("Очікування повідомлень...")
channel.start_consuming()
