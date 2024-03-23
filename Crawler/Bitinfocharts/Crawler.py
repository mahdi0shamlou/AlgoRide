import requests
from bs4 import BeautifulSoup
import json
class CrawlerBitinfoCharts():
    def __init__(self):
        self.Link_req = 'https://bitinfocharts.com/'
    def Get_main_page_html(self):
        print('------ section get html txt of main page ------')
        try:
            resp = requests.get(self.Link_req)
            html_txt = resp.text
            print(f'Response of Site : {resp}')
            return html_txt
        except Exception as e:
            print(f'Error in Get main page Html txt And Error is : {e}')
            return -1
    def Parse_html_main_page(self, html_txt:str):
        print('------ section parse html txt of main page ------')
        soup = BeautifulSoup(html_txt, "lxml")
        elements_t_total = soup.select('tr[id^="t_total"] td') # number of Crypto
        elements_t_price = soup.select('tr[id^="t_price"] td') # Price of crypto
        elements_t_cap = soup.select('tr[id^="t_cap"] td')  # market cap of crypto
        #elements_s = soup.select('tr td')
        #print(len(elements_s))
        print(len(elements_t_cap))
        for e in elements_t_cap:
            print(e.get_text())


test_obj = CrawlerBitinfoCharts()
html_txt = test_obj.Get_main_page_html()
test_obj.Parse_html_main_page(html_txt)