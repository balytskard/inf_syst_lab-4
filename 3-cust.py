import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='stock_platform', exchange_type='topic')

def callback(ch, method, properties, body):
    print(f"Отримано повідомлення з ключем {method.routing_key}: {body.decode()}")

companies = ['apple', 'google', 'amazon']
for company in companies:
    channel.queue_declare(queue=f'{company}_queue')
    
    channel.queue_bind(exchange='stock_platform', queue=f'{company}_queue', routing_key=f'stock.{company}.*')
    
    channel.basic_consume(queue=f'{company}_queue', on_message_callback=callback, auto_ack=True)

print("Очікування повідомлень...")
channel.start_consuming()
