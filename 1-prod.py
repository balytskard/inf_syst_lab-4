import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue_name = 'QUEUE1'  
channel.queue_declare(queue=queue_name)


messages = ["MSG 1", "MSG 2", "MSG 3",
            "MSG 4", "MSG 5", "MSG 6",
            "MSG 7", "MSG 8", "MSG 9",
            "MSG 10", "MSG 11", "MSG 12"]
interval = 2  

for message in messages:
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f"Sent: {message}")
    time.sleep(interval)  

connection.close()
