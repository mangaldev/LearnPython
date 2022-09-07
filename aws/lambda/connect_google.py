import os
from datetime import datetime
from urllib.request import Request, urlopen

SITE = os.environ['site']
EXPECTED = os.environ['expected']


def validate(res):
    return EXPECTED in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        req = Request(SITE, headers={'User-Agent': 'AWS Lambda'})
        res = urlopen(req).read()
        print(str(res))
        if not validate(str(res)):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
