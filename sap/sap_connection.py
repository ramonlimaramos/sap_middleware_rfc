# coding=utf-8

import signal, sys

from os import path
from configparser import ConfigParser
from pyrfc import Server, Connection

class Connection_SAP(object):

    def __init__(self):
        self.__config = ConfigParser()
        self.__config.read(self._read_parameters_connection(), encoding='utf8')

    def get_connection(self):
        """ Returns the SAP connection """
        return Connection(**self.__config._sections['connection'])
    
    def get_gateway(self):
        """ Return the SAP gateway """
        return Server(**self.__config._sections['gateway'])

    def _read_parameters_connection(self, filename='sapnwrfc.cfg'):
        pwd = path.realpath(path.dirname(__file__) + path.sep + '.')
        return path.join(pwd, filename)