import requests
from bs4 import BeautifulSoup
import lxml
import time

import requests

cookies = {
    'qrator_jsr': '1696950389.824.gbwjwTtKFHLAD3Wy-r15ompm8r4tovgsfh0jsj9qnni2ttd6d-00',
    'qrator_ssid': '1696950390.989.zeNu3242pxBnJS3m-5su8n07d9rdcdc9s8a3mhqjur987n70k',
    'qrator_jsid': '1696950389.824.gbwjwTtKFHLAD3Wy-e49gh2oleij3f0phj8b8a1n6d3j629n0',
    'stest201': '1',
    'stest207': 'acc1',
    'stest209': 'ct2',
    'tp_city_id': '36966',
    'PHPSESSID': 'ec268d19967896266e4c9874900fcf53',
    'user_public_id': 'MrugDIhaJc6UFEOw4Nr4jRlyT15JlLrvHBKMXiP58JHx6usuNjWWs%2Bn8ff%2Bk3h3B',
    'expId': 'PRozp8kCSgK4duzzxjym7w',
    'expVar': '1',
    '_slfs': '1696950392952',
    '_slid': '65256879bd5e268c220d91a5',
    '_slsession': '1DD1A79D-6FC5-4BF3-8A52-67CCC2730EE9',
    '_gcl_au': '1.1.96109361.1696950394',
    'uxs_uid': '9a573210-677e-11ee-b78f-351838d6dd97',
    'tmr_lvid': '7a055b70f90bfd355ecb04cabf13b1a0',
    'tmr_lvidTS': '1696950394845',
    '_gid': 'GA1.2.2114564477.1696950395',
    '_ym_uid': '1696950395352243045',
    '_ym_d': '1696950395',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    '_rc_sess': '881f1aad-a976-4ce4-b99a-170de0a075ee',
    '_rc_uid': 'd9bd94c99f2527162227a124a3634c84',
    'afUserId': '9e7e8458-91cc-4db2-acb4-1bf7b111d9e4-p',
    'AF_SYNC': '1696950395941',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    'visitedPagesNumber': '2',
    '_slid_server': '65256879bd5e268c220d91a5',
    'tmr_detect': '1%7C1696950479412',
    '_ga': 'GA1.1.775825937.1696950395',
    '_ga_RD4H4CBNJ3': 'GS1.1.1696950395.1.1.1696950479.58.0.0',
    'mindboxDeviceUUID': '9a544277-95f5-4be1-b2cc-c4effabeb9b1',
    'directCrm-session': '%7B%22deviceGuid%22%3A%229a544277-95f5-4be1-b2cc-c4effabeb9b1%22%7D',
    'pageviewTimer': '148.921',
}

headers = {
    'authority': 'www.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'qrator_jsr=1696950389.824.gbwjwTtKFHLAD3Wy-r15ompm8r4tovgsfh0jsj9qnni2ttd6d-00; qrator_ssid=1696950390.989.zeNu3242pxBnJS3m-5su8n07d9rdcdc9s8a3mhqjur987n70k; qrator_jsid=1696950389.824.gbwjwTtKFHLAD3Wy-e49gh2oleij3f0phj8b8a1n6d3j629n0; stest201=1; stest207=acc1; stest209=ct2; tp_city_id=36966; PHPSESSID=ec268d19967896266e4c9874900fcf53; user_public_id=MrugDIhaJc6UFEOw4Nr4jRlyT15JlLrvHBKMXiP58JHx6usuNjWWs%2Bn8ff%2Bk3h3B; expId=PRozp8kCSgK4duzzxjym7w; expVar=1; _slfs=1696950392952; _slid=65256879bd5e268c220d91a5; _slsession=1DD1A79D-6FC5-4BF3-8A52-67CCC2730EE9; _gcl_au=1.1.96109361.1696950394; uxs_uid=9a573210-677e-11ee-b78f-351838d6dd97; tmr_lvid=7a055b70f90bfd355ecb04cabf13b1a0; tmr_lvidTS=1696950394845; _gid=GA1.2.2114564477.1696950395; _ym_uid=1696950395352243045; _ym_d=1696950395; _ym_isad=1; _ym_visorc=b; _rc_sess=881f1aad-a976-4ce4-b99a-170de0a075ee; _rc_uid=d9bd94c99f2527162227a124a3634c84; afUserId=9e7e8458-91cc-4db2-acb4-1bf7b111d9e4-p; AF_SYNC=1696950395941; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; visitedPagesNumber=2; _slid_server=65256879bd5e268c220d91a5; tmr_detect=1%7C1696950479412; _ga=GA1.1.775825937.1696950395; _ga_RD4H4CBNJ3=GS1.1.1696950395.1.1.1696950479.58.0.0; mindboxDeviceUUID=9a544277-95f5-4be1-b2cc-c4effabeb9b1; directCrm-session=%7B%22deviceGuid%22%3A%229a544277-95f5-4be1-b2cc-c4effabeb9b1%22%7D; pageviewTimer=148.921',
    'dnt': '1',
    'if-none-match': '"11440b-4P9xVqJAj0Eid3rICV2tbpi37Qc"',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}


products = {}
for i in range(1, 24):
    params = {
        'p': str(i),
    }
    time.sleep(1)
    print(f"собираю данные со страницы {i}")
    response = requests.get('https://www.technopark.ru/smartfony/', cookies=cookies, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text,"lxml")
    container = soup.find("div",class_="catalog-listing")
    cards = container.find_all("div",class_="product-card-big__container")
    for card in cards:
        name = card.find("div",class_ = "product-card-big__name").text.strip()
        price = card.find("div",class_="product-prices__price").text.strip()[:7]
        products[name]=price
print(products)