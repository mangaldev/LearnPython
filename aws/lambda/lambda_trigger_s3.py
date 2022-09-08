import os
from datetime import datetime
from urllib.request import Request, urlopen


def lambda_handler(event, context):
    print('Received Event {}...'.format(event))
