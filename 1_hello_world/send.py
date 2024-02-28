#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel() # We are connected to the server

channel.queue_declare(queue='hello') # creating queue

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!') # this the message sending
print(" [x] Sent 'Hello World!'")
connection.close() # close connection


