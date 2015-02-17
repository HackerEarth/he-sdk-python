import json
import urllib
import urllib2
import requests

from settings import COMPILE_API_ENDPOINT
from settings import RUN_API_ENDPOINT
from settings import CLIENT_SECRET

from result import CompileResult
from result import RunResult


class HackerEarthAPI(object):
    def __init__(self, params):
        self.params_dict = params.get_params()

    def compile(self):
        response = self.__request(COMPILE_API_ENDPOINT, self.params_dict)
        result = CompileResult(response)
        return result

    def run(self):
        response = self.__request(RUN_API_ENDPOINT, self.params_dict)
        result = RunResult(response)
        return result

    def __request(self, url, params):
        try:
            response = requests.post(url, data=params)
        except Exception, e:
            print e
        return response.text


    def __result(self, res):
        result = json.load(res)
        return result
