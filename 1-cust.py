import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue_name = 'QUEUE1' 
channel.queue_declare(queue=queue_name)


message_count = 0


def callback(ch, method, properties, body):
    global message_count
    message_count += 1
    print(f"Received {message_count}: {body.decode()}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(f"Waiting for messages in queue: {queue_name}")
channel.start_consuming()
