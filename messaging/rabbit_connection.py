# coding=utf-8

import pika

from os import path
from configparser import ConfigParser


class Singleton(object):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(
                Singleton, class_).__new__(class_, *args) #, **kwargs
        
        return class_._instances[class_]


class Rabbit_Template(Singleton):

    def __init__(self, exchange='rfc_notify_result'):

        self.__config = ConfigParser()
        self.__exchange = exchange
        self.__exchange_type = 'fanout'
        self.__routing_key = ''
        self.__config.read(
            self.__read_parameters_connection(), encoding='utf8')
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(**self.__config._sections['connection']))

    def __read_parameters_connection(self, filename='rabbitconfig.cfg'):

        pwd = path.realpath(path.dirname(__file__) + path.sep + '.')
        return path.join(pwd, filename)

    @property
    def exchange(self):

        return self.__exchange

    @property
    def exchange_type(self):

        return self.__exchange_type

    @property
    def routing_key(self):

        return self.__routing_key

    def get_connection(self):
        """ Returns rabbitmq connection """

        return self.__connection

    def set_channel(self):
        """ Set the channel for connection """

        channel = self.__connection.channel()
        channel.exchange_declare(exchange=self.__exchange,
                                 exchange_type=self.__exchange_type)
        return channel
