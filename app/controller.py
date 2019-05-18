# coding=utf-8

import json
import _thread

from os import path
from flask import request, jsonify, send_from_directory
from flask_cors import cross_origin
from app import server
from sap.sap_adapter import RFC
from messaging.rabbit import Publish


class Index(object):

    @server.route('/')
    @server.route('/index')
    def index(self=None):
        return '<h1>Index</h1>'

    @server.route('/favicon.ico')
    def favicon(self=None):
        return send_from_directory(path.join(server.root_path, 'static'), 'favicon.ico')


class RFC_Web(object):

    @server.route('/sap-invoke/notification/install/<rfc_name>', methods=['POST'])
    def rfc_notification(self=None, rfc_name=None):
        try:
            _thread.start_new_thread(RFC().notification_func,
                                    (rfc_name, RFC_Web._notification_result))
            return jsonify({'result': 'RFC function sucessful installed, queued to broker'})
        except Exception as e:
            return e

    @server.route('/sap-invoke/notification/starter/<starter>', methods=['POST'])
    def rfc_notify_func(self=None, starter=None):
        try:
            print(starter, request.json)
            if request.json is not None:
                RFC().invoke_func(starter, request.json)
                return jsonify({'result': 'RFC function sucessful installed, queued to broker'})
                
            else:
                return Error_Handler().not_content(error='I_RFC field is required')

        except Exception as e:
            return e

    @server.route('/sap-invoke/rfc/<rfc_name>', methods=['POST', 'OPTIONS'])
    @cross_origin()
    def rfc_invoke_sync(self=None, rfc_name=None):
        try:
            return jsonify(RFC().invoke_func(rfc_name.upper(), request.json))
        except Exception as e:
            return e

    def _notification_result(self=None, request_context=None, **args):
        """" Develop Rabbit broker """
        sender = Publish()
        sender.set_message(jsonify(args))
        sender.send()


class Error_Handler(object):

    @server.errorhandler(411)
    def not_content(self, error=None):
        res = jsonify(error)
        res.status_code = 411
        return res
