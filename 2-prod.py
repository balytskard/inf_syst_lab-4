import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

messages = [
    ('stock.apple.buy', 'Buy Apple stocks'),
    ('stock.google.sell', 'Sell Google stocks'),
    ('stock.amazon.buy', 'Buy Amazon stocks'),
    ('stock.apple.sell', 'Sell Apple stocks')
]

for routing_key, message in messages:
    channel.basic_publish(exchange='stock_exchange', routing_key=routing_key, body=message)
    print(f"Відправлено повідомлення: {message} з ключем {routing_key}")

connection.close()
