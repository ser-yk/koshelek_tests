from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time

from sys import getsizeof
from datetime import datetime
import json


def some_tests():
    try:
        response = get_response()
        time_answer = response.elapsed.total_seconds()
        assert time_answer < 5, f'The server takes too long to respond: {time_answer} sec'

        size = getsizeof(response.content) / 1024
        assert size < 10, f'The size of the response data exceeds 10KB. Actual: {size:.2f} KB'

        data = json.loads(response.text)
        today = datetime.now().strftime("%Y-%m-%d")
        for i in data['data']:
            date = datetime.strptime(i['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
            assert date == today, f'The date currency - "{i["name"]}" is not actual: {i["last_updated"]}'
        return time_answer
    except:
        return None

def get_response():
    key = 'c7a24b51-3db0-4cdf-b814-78730f0e8014'
    url = 'https://pro-api.coinmarketcap.com//v1/cryptocurrency/listings/latest'
    parameters = {
        'limit': 10,
        'sort': 'volume_24h'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        return response
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)