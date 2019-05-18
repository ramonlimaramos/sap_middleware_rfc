# coding=utf-8

from sap.sap_connection import Connection_SAP


class RFC(object):

    def __init__(self):
        self.__connection = Connection_SAP().get_connection()
        self.__gateway = Connection_SAP().get_gateway()

    def invoke_func(self, name, imp):
        try:
            with self.__connection as con:
                return con.call(name, **imp)
        except Exception as e:
            raise e

    def notification_func(self, name, function_executor):
        try:
            with self.__connection as con:
                description = con.get_function_description(name)
                with self.__gateway as server:
                    server.install_function(description, function_executor)
                    server.serve()
        except Exception as e:
            raise e

    def start_serving(self):
        try:
            with self.__gateway as server:
                server.serve()
        except Exception as e:
            raise e
