import requests
import json

cookies = {
    'i': 'QgaUQqKCcY8J97GVaBZydVcqD/HhKfocZi5jJqFOXZXc/8azegezbVR/FLw9hG7iHGYC0NikRdsz/fSciVFGk2MailI=',
    'yandexuid': '6026198801695236084',
    'yuidss': '6026198801695236084',
    'ymex': '2010596087.yrts.1695236087',
    'gdpr': '0',
    '_ym_isad': '1',
    '_ym_uid': '1695236087728577582',
    '_ym_visorc': 'b',
    '_ym_d': '1695236088',
    '_yasc': 'riFKXdLY9LMNDg5hsx0PO5WJF8C3XvsJMSIE/0hNdypMdGWPuLSZFaIM/55UuzJbdgc=',
    'Session_id': '3:1695236537.5.0.1695236537650:Ys6uVQ:86.1.2:1|1428485112.-1.2.1:292766768.3:1695236537|3:10276041.481801.9cih4yzxv9w2_r_aeKv6gCYvBTs',
    'sessar': '1.1182.CiDbdHygHY0fgOGQF4jywf6uMxovnGw6zp4P3FwZyAz5CA.NsfszMK1u0Y0kDUvHQTVUo7B2MdLr6IIRsHG_Qgzohg',
    'sessionid2': '3:1695236537.5.0.1695236537650:Ys6uVQ:86.1.2:1|1428485112.-1.2.1:292766768.3:1695236537|3:10276041.481801.fakesign0000000000000000000',
    'yp': '2010596537.udn.cDpsaW5hcHVzaDIwMDJwdXNoa2FyZXZh',
    'L': 'WxRnUXMNX2JjWUJmWANRfngPZg0ATAtWOlolBxonFDhYZ2gKPh0mOS8oR1APEA==.1695236537.15471.342099.35ad8a551ce685ae467e45ea705ab965',
    'yandex_login': 'linapush2002pushkareva',
    'ys': 'udn.cDpsaW5hcHVzaDIwMDJwdXNoa2FyZXZh#c_chck.1148802226',
    'lastVisitedPage': '%7B%7D',
    'device_id': 'a325776453509544bd81b6b0a4187f3c610795aa9',
    'active-browser-timestamp': '1695236541855',
    'bh': 'Ej8iR29vZ2xlIENocm9tZSI7dj0iMTA3IiwiQ2hyb21pdW0iO3Y9IjEwNyIsIk5vdD1BP0JyYW5kIjt2PSIyNCIaBSJ4ODYiIhAiMTA3LjAuNTMwNC4xMTAiKgI/MDoHIkxpbnV4IkIIIjUuMTMuMCJKBCI2NCJSXCJHb29nbGUgQ2hyb21lIjt2PSIxMDcuMC41MzA0LjExMCIsIkNocm9taXVtIjt2PSIxMDcuMC41MzA0LjExMCIsIk5vdD1BP0JyYW5kIjt2PSIyNC4wLjAuMCIi',
    'is_gdpr': '0',
    'is_gdpr_b': 'CLaqFBDGzwE=',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'i=QgaUQqKCcY8J97GVaBZydVcqD/HhKfocZi5jJqFOXZXc/8azegezbVR/FLw9hG7iHGYC0NikRdsz/fSciVFGk2MailI=; yandexuid=6026198801695236084; yuidss=6026198801695236084; ymex=2010596087.yrts.1695236087; gdpr=0; _ym_isad=1; _ym_uid=1695236087728577582; _ym_visorc=b; _ym_d=1695236088; _yasc=riFKXdLY9LMNDg5hsx0PO5WJF8C3XvsJMSIE/0hNdypMdGWPuLSZFaIM/55UuzJbdgc=; Session_id=3:1695236537.5.0.1695236537650:Ys6uVQ:86.1.2:1|1428485112.-1.2.1:292766768.3:1695236537|3:10276041.481801.9cih4yzxv9w2_r_aeKv6gCYvBTs; sessar=1.1182.CiDbdHygHY0fgOGQF4jywf6uMxovnGw6zp4P3FwZyAz5CA.NsfszMK1u0Y0kDUvHQTVUo7B2MdLr6IIRsHG_Qgzohg; sessionid2=3:1695236537.5.0.1695236537650:Ys6uVQ:86.1.2:1|1428485112.-1.2.1:292766768.3:1695236537|3:10276041.481801.fakesign0000000000000000000; yp=2010596537.udn.cDpsaW5hcHVzaDIwMDJwdXNoa2FyZXZh; L=WxRnUXMNX2JjWUJmWANRfngPZg0ATAtWOlolBxonFDhYZ2gKPh0mOS8oR1APEA==.1695236537.15471.342099.35ad8a551ce685ae467e45ea705ab965; yandex_login=linapush2002pushkareva; ys=udn.cDpsaW5hcHVzaDIwMDJwdXNoa2FyZXZh#c_chck.1148802226; lastVisitedPage=%7B%7D; device_id=a325776453509544bd81b6b0a4187f3c610795aa9; active-browser-timestamp=1695236541855; bh=Ej8iR29vZ2xlIENocm9tZSI7dj0iMTA3IiwiQ2hyb21pdW0iO3Y9IjEwNyIsIk5vdD1BP0JyYW5kIjt2PSIyNCIaBSJ4ODYiIhAiMTA3LjAuNTMwNC4xMTAiKgI/MDoHIkxpbnV4IkIIIjUuMTMuMCJKBCI2NCJSXCJHb29nbGUgQ2hyb21lIjt2PSIxMDcuMC41MzA0LjExMCIsIkNocm9taXVtIjt2PSIxMDcuMC41MzA0LjExMCIsIk5vdD1BP0JyYW5kIjt2PSIyNC4wLjAuMCIi; is_gdpr=0; is_gdpr_b=CLaqFBDGzwE=',
    'DNT': '1',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Current-UID': '1428485112',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-09-20T22:02:40+03:00',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.14762147707982232',
}



response = requests.post('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers).json()
track_info = {"имя_исполнителя": response["chartPositions"][0]["track"]["artists"][0]["name"],"название_трека": response["chartPositions"][0]["track"]["title"]}

with open("data.json", 'w') as f:
    json.dump(track_info, f, ensure_ascii=False)
print(track_info)
