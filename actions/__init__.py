from flask import Flask
from flask_cors import CORS
from rasa.core.agent import Agent

app = Flask(__name__)
CORS(app)