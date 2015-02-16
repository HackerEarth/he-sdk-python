import json
import urllib
import urllib2
import requests

from settings import COMPILE_API_ENDPOINT
from settings import RUN_API_ENDPOINT
from settings import CLIENT_SECRET


class HackerEarthAPI(object):
    def __init__(self, params):
        self.params_dict = params.get_params()

    def compile(self):
        data = self.__request(COMPILE_API_ENDPOINT, self.params_dict)
        return data

    def run(self):
        data = self.__request(RUN_API_ENDPOINT, self.params_dict)
        return data

    def __request(self, url, params):
        try:
            response = requests.post(url, data=params)
        except Exception, e:
            print e
        print response.text
        return response


    def __result(self, res):
        result = json.load(res)
        return result
