import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchange_name = 'general_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

queue1_name = 'queue1'
channel.queue_declare(queue=queue1_name, durable=True)

queue2_name = 'queue2'
channel.queue_declare(queue=queue2_name, durable=True)

channel.queue_bind(exchange=exchange_name, queue=queue1_name, routing_key='task.one')
channel.queue_bind(exchange=exchange_name, queue=queue2_name, routing_key='task.two')

print(f"Exchange '{exchange_name}' and queues '{queue1_name}' and '{queue2_name}' created and bound.")

connection.close()