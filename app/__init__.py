import os

import boto3
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv('TOKEN')
TABLE_NAME = os.getenv('TABLE_NAME')
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table(TABLE_NAME)

from app.routes import *
from app.cli_commands import *
