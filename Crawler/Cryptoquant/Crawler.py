import requests
import json


class CrawlerCryptoQuant():
    def __init__(self):
        self.Link_req_now_price = 'http://live-api.cryptoquant.com/api/v2/assets/61712eb35a176168a02409e8/now-price'
        self.Link_req_metric = 'http://live-api.cryptoquant.com/api/v2/assets/61712eb35a176168a02409e8/metrics'
    def Send_request_now_price(self):# this methode get live price of asset
        try:
            headers = {
                'Host':'live-api.cryptoquant.com',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
            }
            resp = requests.get(self.Link_req_now_price, headers=headers)
            resp = json.loads(resp.text)
            print(resp)
            return resp
        except Exception as E:
            print(f'Error in Get data from Cryptoquant And Error is : {E}')
            return -1
    def Send_request_metrics(self):# this methode get all metrics and all charts in crypto quant all data about charts get in this method
        try:
            headers = {
                'Host':'live-api.cryptoquant.com',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
            }
            resp = requests.get(self.Link_req_metric, headers=headers)
            resp = json.loads(resp.text)# has 16 section
            ''' # print like json rows in console python
            pretty_json = json.dumps(resp[0], indent=4, sort_keys=True)
            print(pretty_json)
            '''
            for i in resp:
                name = i['category']['name']['en']
                desc = i['category']['description']['en']
                metrics_one = i['category']['metrics'][0]['title']['en']
                print(f'Name section of metrics : {name} \n And Desc is : {desc} \n And Metrics one is : {metrics_one}\n')
                print('-------------------------------------------------------------------------------------------------')



            return resp
        except Exception as E:
            print(f'Error in Get data from Cryptoquant And Error is : {E}')
            return -1
x = CrawlerCryptoQuant()
x.Send_request_now_price()
x.Send_request_metrics()