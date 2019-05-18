# coding=utf-8

import pika
from messaging.rabbit_connection import Rabbit_Template


class Publish(Rabbit_Template):

    def __init__(self, exchange):

        super(Publish, self).__init__(exchange=exchange)
        self.__body = None
        self.__properties = pika.BasicProperties(delivery_mode=2)

    def set_message(self, message):

        self.__body = message

    def send(self):

        with super(Publish, self).set_channel() as channel:
            channel.basic_publish(exchange=super(Publish, self).exchange,
                                  routing_key=super(Publish, self).routing_key,
                                  body=self.__body)

            print('[sap_server_func]{Messaging} Notification result emited')


class Subscribe(Rabbit_Template):

    def __init__(self, exchange):

        super(Subscribe, self).__init__(exchange=exchange)
        self.__callback = None

    def set_callback(self, callback):

        self.__callback = callback

    def consume(self):

        with super(Subscribe, self).set_channel() as channel:
            
            result = channel.queue_declare(exclusive=True)
            channel.queue_bind(exchange=super(Subscribe, self).exchange,
                               queue=result.method.queue)

            channel.basic_consume(
                self.__callback, queue=result.method.queue, no_ack=True)
            
            print('[sap_server_func]{Messaging} Consumition started')
            channel.start_consuming()

