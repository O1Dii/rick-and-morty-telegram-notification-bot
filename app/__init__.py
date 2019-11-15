import os

import boto3
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv('TOKEN')
TABLE_NAME = os.getenv('TABLE_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

dynamodb = boto3.resource('dynamodb',
                          region_name='eu-central-1',
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
table = dynamodb.Table(TABLE_NAME)

from app.routes import *
from app.cli_commands import *
