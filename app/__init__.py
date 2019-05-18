# coding=utf-8

from flask import Flask
from flask_cors import CORS

server = Flask(__name__)
CORS(server)

from app import controller

controller.Index()
controller.RFC_Web()