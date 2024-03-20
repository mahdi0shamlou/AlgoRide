import requests



class CrawlerCryptoQuant():

    def __init__(self):

        self.Link_req_metric = 'http://live-api.cryptoquant.com/api/v2/assets/61712eb35a176168a02409e8/metrics'
        self.Link_req_now_price = 'http://live-api.cryptoquant.com/api/v2/assets/61712eb35a176168a02409e8/now-price'

    def send_requests(self):
        headers = {
            'Host':'live-api.cryptoquant.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
        }
        resp = requests.get(self.Link_req_now_price, headers=headers)
        print(resp.text)

x = CrawlerCryptoQuant()
x.send_requests()