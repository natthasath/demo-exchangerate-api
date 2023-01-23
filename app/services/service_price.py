from decouple import config
from fastapi.responses import JSONResponse
import requests
import xmltodict
import json

class ExchangeService:
    def __init__(self):
        self.api_exchange = config("API_EXCHANGE")

    def get_all(self):
        response = requests.get(self.api_exchange)
        data = json.loads(response.content)
        return data['conversion_rates']

    def get_search(self, name):
        response = requests.get(self.api_exchange)
        data = json.loads(response.content)
        for key in data['conversion_rates']:
            if name == key:
                return data['conversion_rates'][name]

        return JSONResponse(status_code=404, content={"message": "Resource not found"})

    def get_pair(self):
        url = 'https://v6.exchangerate-api.com/v6/ac603e9c0de51d5495043231/pair/THB/USD'
        response = requests.get(url)
        data = json.loads(response.content)
        return data

class OilService:
    def __init__(self):
        self.api_oil = config("API_OIL")

    def get_all(self):
        response = requests.get(self.api_oil)
        data = xmltodict.parse(response.content)
        return data['header']['item']

    def get_search(self, name):
        response = requests.get(self.api_oil)
        data = xmltodict.parse(response.content)
        for key in range(len(data['header']['item'])):
            if name == data['header']['item'][key]['type']:
                return data['header']['item'][key]

        return JSONResponse(status_code=404, content={"message": "Resource not found"})

class GoldService:
    def __init__(self):
        self.api_gold = config("API_GOLD")