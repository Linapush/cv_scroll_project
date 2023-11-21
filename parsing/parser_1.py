# import requests
# import json

# cookies = {
#     'stest201': '1',
#     'stest207': 'acc1',
#     'stest209': 'ct1',
#     'tp_city_id': '36966',
#     'PHPSESSID': 'accf3c793c64032d7ffb05c8f8c5c6d3',
#     'user_public_id': 'z7zUmrUA3WL1lN1ph6YlwqKsVSdxlajZcGOfCiyeTNKj6rk6X%2BI5JmEKePK9HNsR',
#     'expId': 'vd5GSoZtQLaTauxUbJKZQA',
#     'expVar': '1',
#     '_slid': '650ae30ed0dd3a7f73016bdb',
#     '_slid_server': '650ae30ed0dd3a7f73016bdb',
#     '_gcl_au': '1.1.1608167319.1695212304',
#     'uxs_uid': 'cbd7b9b0-57af-11ee-a9fd-5f6e5be35beb',
#     '_ym_uid': '169521230599172291',
#     '_ym_d': '1695212305',
#     'tmr_lvid': '1c5e99dfa7dd8b9698c183ba4bc15cb3',
#     'tmr_lvidTS': '1695212304688',
#     '_gid': 'GA1.2.758112897.1695212305',
#     '_ym_isad': '1',
#     'afUserId': 'bd724f49-e21a-4b6a-9c8b-b88f09a6d910-p',
#     'AF_SYNC': '1695212305967',
#     '_userGUID': '0:lmrpn0ha:sPSQxhANMkvOx_E1oCU9luchxXC5LhEW',
#     'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20a3b6e142cdd6ead78eec%22}',
#     'qrator_jsr': '1695221320.054.kA0G5kpkyH3lQoFa-6i3nav9ttpneuf7ftggnhoi1ictqk2ar-00',
#     'qrator_jsid': '1695221320.054.kA0G5kpkyH3lQoFa-8kpoosp15ovkbq78ct7oaq795tkp04d1',
#     '_slsession': '38F21C54-502D-4D61-98E5-6FAC8056FDAC',
#     '_ym_visorc': 'b',
#     'pageviewTimerFired15': 'true',
#     'pageviewTimerFired30': 'true',
#     'dSesn': '56376d50-b2b4-7037-d8f8-6a727e2c8fb5',
#     '_dvs': '0:lmrv11ev:S9uB9lOkTweXe~ufbvANDefR7C3rMK2l',
#     'visitedPagesNumber': '9',
#     '_ga': 'GA1.1.913433631.1695212305',
#     '_ga_RD4H4CBNJ3': 'GS1.1.1695221324.3.1.1695221364.20.0.0',
#     'tmr_detect': '0%7C1695221366652',
#     'digi_uc': 'W1siY3YiLCI1NzcxOTAiLDE2OTUyMjEzNjc5MTZdXQ==',
#     'mindboxDeviceUUID': 'f3386124-5a52-4bdd-9e2c-4fab58b2d287',
#     'directCrm-session': '%7B%22deviceGuid%22%3A%22f3386124-5a52-4bdd-9e2c-4fab58b2d287%22%7D',
#     'pageviewTimer': '71.277',
#     'pageviewTimerFired60': 'true',
# }

# headers = {
#     'authority': 'www.technopark.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'stest201=1; stest207=acc1; stest209=ct1; tp_city_id=36966; PHPSESSID=accf3c793c64032d7ffb05c8f8c5c6d3; user_public_id=z7zUmrUA3WL1lN1ph6YlwqKsVSdxlajZcGOfCiyeTNKj6rk6X%2BI5JmEKePK9HNsR; expId=vd5GSoZtQLaTauxUbJKZQA; expVar=1; _slid=650ae30ed0dd3a7f73016bdb; _slid_server=650ae30ed0dd3a7f73016bdb; _gcl_au=1.1.1608167319.1695212304; uxs_uid=cbd7b9b0-57af-11ee-a9fd-5f6e5be35beb; _ym_uid=169521230599172291; _ym_d=1695212305; tmr_lvid=1c5e99dfa7dd8b9698c183ba4bc15cb3; tmr_lvidTS=1695212304688; _gid=GA1.2.758112897.1695212305; _ym_isad=1; afUserId=bd724f49-e21a-4b6a-9c8b-b88f09a6d910-p; AF_SYNC=1695212305967; _userGUID=0:lmrpn0ha:sPSQxhANMkvOx_E1oCU9luchxXC5LhEW; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20a3b6e142cdd6ead78eec%22}; qrator_jsr=1695221320.054.kA0G5kpkyH3lQoFa-6i3nav9ttpneuf7ftggnhoi1ictqk2ar-00; qrator_jsid=1695221320.054.kA0G5kpkyH3lQoFa-8kpoosp15ovkbq78ct7oaq795tkp04d1; _slsession=38F21C54-502D-4D61-98E5-6FAC8056FDAC; _ym_visorc=b; pageviewTimerFired15=true; pageviewTimerFired30=true; dSesn=56376d50-b2b4-7037-d8f8-6a727e2c8fb5; _dvs=0:lmrv11ev:S9uB9lOkTweXe~ufbvANDefR7C3rMK2l; visitedPagesNumber=9; _ga=GA1.1.913433631.1695212305; _ga_RD4H4CBNJ3=GS1.1.1695221324.3.1.1695221364.20.0.0; tmr_detect=0%7C1695221366652; digi_uc=W1siY3YiLCI1NzcxOTAiLDE2OTUyMjEzNjc5MTZdXQ==; mindboxDeviceUUID=f3386124-5a52-4bdd-9e2c-4fab58b2d287; directCrm-session=%7B%22deviceGuid%22%3A%22f3386124-5a52-4bdd-9e2c-4fab58b2d287%22%7D; pageviewTimer=71.277; pageviewTimerFired60=true',
#     'dnt': '1',
#     'if-none-match': '"1078d5-Z8BbHTdYlBmTiLasN+i4goEiAUQ"',
#     'referer': 'https://www.technopark.ru/',
#     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
# }

# response = requests.get('https://www.technopark.ru/smartfony/', cookies=cookies, headers=headers)
# print(response)
# with open("data.json", "w") as f:
#     json.dump(response, f, ensure_ascii=False)
# print(response.text)
# Convert curl commands to Python
# находим запрос, который хотим отправить
# response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers, json=json_data)
# print(response.text)

# import requests
# import json

# cookies = {
#     'stest201': '1',
#     'stest207': 'acc1',
#     'stest209': 'ct1',
#     'tp_city_id': '36966',
#     'PHPSESSID': 'accf3c793c64032d7ffb05c8f8c5c6d3',
#     'user_public_id': 'z7zUmrUA3WL1lN1ph6YlwqKsVSdxlajZcGOfCiyeTNKj6rk6X%2BI5JmEKePK9HNsR',
#     'expId': 'vd5GSoZtQLaTauxUbJKZQA',
#     'expVar': '1',
#     '_slid': '650ae30ed0dd3a7f73016bdb',
#     '_slid_server': '650ae30ed0dd3a7f73016bdb',
#     '_gcl_au': '1.1.1608167319.1695212304',
#     'uxs_uid': 'cbd7b9b0-57af-11ee-a9fd-5f6e5be35beb',
#     '_ym_uid': '169521230599172291',
#     '_ym_d': '1695212305',
#     'tmr_lvid': '1c5e99dfa7dd8b9698c183ba4bc15cb3',
#     'tmr_lvidTS': '1695212304688',
#     '_gid': 'GA1.2.758112897.1695212305',
#     '_ym_isad': '1',
#     'afUserId': 'bd724f49-e21a-4b6a-9c8b-b88f09a6d910-p',
#     'AF_SYNC': '1695212305967',
#     '_userGUID': '0:lmrpn0ha:sPSQxhANMkvOx_E1oCU9luchxXC5LhEW',
#     'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20a3b6e142cdd6ead78eec%22}',
#     'qrator_jsr': '1695221320.054.kA0G5kpkyH3lQoFa-6i3nav9ttpneuf7ftggnhoi1ictqk2ar-00',
#     'qrator_jsid': '1695221320.054.kA0G5kpkyH3lQoFa-8kpoosp15ovkbq78ct7oaq795tkp04d1',
#     '_slsession': '38F21C54-502D-4D61-98E5-6FAC8056FDAC',
#     '_ym_visorc': 'b',
#     'pageviewTimerFired15': 'true',
#     'pageviewTimerFired30': 'true',
#     'dSesn': '56376d50-b2b4-7037-d8f8-6a727e2c8fb5',
#     '_dvs': '0:lmrv11ev:S9uB9lOkTweXe~ufbvANDefR7C3rMK2l',
#     'visitedPagesNumber': '9',
#     '_ga': 'GA1.1.913433631.1695212305',
#     '_ga_RD4H4CBNJ3': 'GS1.1.1695221324.3.1.1695221364.20.0.0',
#     'tmr_detect': '0%7C1695221366652',
#     'digi_uc': 'W1siY3YiLCI1NzcxOTAiLDE2OTUyMjEzNjc5MTZdXQ==',
#     'mindboxDeviceUUID': 'f3386124-5a52-4bdd-9e2c-4fab58b2d287',
#     'directCrm-session': '%7B%22deviceGuid%22%3A%22f3386124-5a52-4bdd-9e2c-4fab58b2d287%22%7D',
#     'pageviewTimer': '71.277',
#     'pageviewTimerFired60': 'true',
# }

# headers = {
#     'authority': 'www.technopark.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'stest201=1; stest207=acc1; stest209=ct1; tp_city_id=36966; PHPSESSID=accf3c793c64032d7ffb05c8f8c5c6d3; user_public_id=z7zUmrUA3WL1lN1ph6YlwqKsVSdxlajZcGOfCiyeTNKj6rk6X%2BI5JmEKePK9HNsR; expId=vd5GSoZtQLaTauxUbJKZQA; expVar=1; _slid=650ae30ed0dd3a7f73016bdb; _slid_server=650ae30ed0dd3a7f73016bdb; _gcl_au=1.1.1608167319.1695212304; uxs_uid=cbd7b9b0-57af-11ee-a9fd-5f6e5be35beb; _ym_uid=169521230599172291; _ym_d=1695212305; tmr_lvid=1c5e99dfa7dd8b9698c183ba4bc15cb3; tmr_lvidTS=1695212304688; _gid=GA1.2.758112897.1695212305; _ym_isad=1; afUserId=bd724f49-e21a-4b6a-9c8b-b88f09a6d910-p; AF_SYNC=1695212305967; _userGUID=0:lmrpn0ha:sPSQxhANMkvOx_E1oCU9luchxXC5LhEW; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20a3b6e142cdd6ead78eec%22}; qrator_jsr=1695221320.054.kA0G5kpkyH3lQoFa-6i3nav9ttpneuf7ftggnhoi1ictqk2ar-00; qrator_jsid=1695221320.054.kA0G5kpkyH3lQoFa-8kpoosp15ovkbq78ct7oaq795tkp04d1; _slsession=38F21C54-502D-4D61-98E5-6FAC8056FDAC; _ym_visorc=b; pageviewTimerFired15=true; pageviewTimerFired30=true; dSesn=56376d50-b2b4-7037-d8f8-6a727e2c8fb5; _dvs=0:lmrv11ev:S9uB9lOkTweXe~ufbvANDefR7C3rMK2l; visitedPagesNumber=9; _ga=GA1.1.913433631.1695212305; _ga_RD4H4CBNJ3=GS1.1.1695221324.3.1.1695221364.20.0.0; tmr_detect=0%7C1695221366652; digi_uc=W1siY3YiLCI1NzcxOTAiLDE2OTUyMjEzNjc5MTZdXQ==; mindboxDeviceUUID=f3386124-5a52-4bdd-9e2c-4fab58b2d287; directCrm-session=%7B%22deviceGuid%22%3A%22f3386124-5a52-4bdd-9e2c-4fab58b2d287%22%7D; pageviewTimer=71.277; pageviewTimerFired60=true',
#     'dnt': '1',
#     'if-none-match': '"1078d5-Z8BbHTdYlBmTiLasN+i4goEiAUQ"',
#     'referer': 'https://www.technopark.ru/',
#     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
# }

# response = requests.get('https://www.technopark.ru/smartfony/', cookies=cookies, headers=headers)
# print(response)
# with open("data.json", "w") as f:
#     json.dump(response, f, ensure_ascii=False)
# print(response.text)
# Convert curl commands to Python
# находим запрос, который хотим отправить
# response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers, json=json_data)
# print(response.text)

import requests
import json

cookies = {
    '_yasc': 'jONaA4tdvf4kMwgHUSm+WJjlymNIVPPk/WVqNhvUhNLznZV0kQtw9sny2bPcBtJjN2w=',
    'i': 'GBy6KlsNoCBLTOEpACyyk42SVvJVq4kNqc52syIyimp0zbO2HIcUue9Q6zhhH5cVoBd/1ggwJu7556G+MQ/5Zudq+XU=',
    'yandexuid': '7274016051693477910',
    'yuidss': '7274016051693477910',
    'ymex': '2008837912.yrts.1693477912',
    '_ym_uid': '1693477912738478716',
    '_ym_d': '1693477913',
    'yabs-sid': '1127128851695231246',
    'device_id': 'be3e8f486408527612372be1e33f5391e496ea1a1',
    'active-browser-timestamp': '1695232017447',
    'gdpr': '0',
    '_ym_visorc': 'b',
    'is_gdpr': '0',
    'is_gdpr_b': 'CLaqFBDEzwE=',
    '_ym_isad': '2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://music.yandex.ru/chart',
    'Origin': 'https://music.yandex.ru',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': '_yasc=jONaA4tdvf4kMwgHUSm+WJjlymNIVPPk/WVqNhvUhNLznZV0kQtw9sny2bPcBtJjN2w=; i=GBy6KlsNoCBLTOEpACyyk42SVvJVq4kNqc52syIyimp0zbO2HIcUue9Q6zhhH5cVoBd/1ggwJu7556G+MQ/5Zudq+XU=; yandexuid=7274016051693477910; yuidss=7274016051693477910; ymex=2008837912.yrts.1693477912; _ym_uid=1693477912738478716; _ym_d=1693477913; yabs-sid=1127128851695231246; device_id=be3e8f486408527612372be1e33f5391e496ea1a1; active-browser-timestamp=1695232017447; gdpr=0; _ym_visorc=b; is_gdpr=0; is_gdpr_b=CLaqFBDEzwE=; _ym_isad=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    # 'Content-Length': '0',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

# response = requests.post(
#     'https://mc.yandex.ru/watch/26812653?page-url=https%3A%2F%2Fmusic.yandex.ru%2Fchart&charset=utf-8&ut=noindex&hittoken=1695232016_d35ec1edb4b287216fefb20dac0240e9e84baa43a8909c14c5a3df5e4e1b9115&browser-info=nb%3A1%3Acl%3A103%3Aar%3A1%3Avf%3A3qm6qq812ez2u52wds05w4b%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A1111%3Acn%3A1%3Adp%3A0%3Als%3A981356522747%3Ahid%3A142943078%3Az%3A180%3Ai%3A20230920204711%3Aet%3A1695232032%3Ac%3A1%3Arn%3A101118423%3Arqn%3A12%3Au%3A1693477912738478716%3Aw%3A1844x156%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Aco%3A0%3Acpf%3A1%3Antf%3A1%3Aeu%3A0%3Ans%3A1695232015489%3Aadb%3A2%3Apu%3A16037005741693477912738478716%3Azzlc%3Ana%3Acc%3A2586023931695231500%3Arqnl%3A1%3Ast%3A1695232032&t=gdpr(3%2C3-0)mc(p-14-h-3)clc(0-0-0)rqnt(3)aw(1)fid(400)ti(0)&force-urlencoded=1',
#     cookies=cookies,
#     headers=headers,
# )
# # with open("data.json", "w") as f:
# #     json.dump(response, f, ensure_ascii=False)
# # print(response.text)
# data = response.json()

# with open("data.json", "w") as f:
#     json.dump(data, f, ensure_ascii=False)

# print(response.text)


response = requests.post(
    'https://music.yandex.ru/chart', cookies=cookies, headers=headers)
if response.status_code == 200:
    try:        
        data = response.json()        
        with open("data.json", "w") as f:            
            json.dump(data, f, ensure_ascii=False)    
    except json.JSONDecodeError as e:        
        print("Не удалось разобрать содержимое ответа как JSON.")       
    print("\nСодержимое ответа:\n", response.content.decode())
else:    print("Запрос завершился с кодом состояния:", response.status_code)

# import requests

# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fi;q=0.6,nb;q=0.5,is;q=0.4,pt;q=0.3,ro;q=0.2,it;q=0.1,de;q=0.1',
#     'Connection': 'keep-alive',
#     'Referer': 'https://music.yandex.ru/chart',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'X-Current-UID': '403036463',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Retpath-Y': 'https://music.yandex.ru/chart',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
# }

# params = {
#     'what': 'chart',
#     'lang': 'ru',
#     'external-domain': 'music.yandex.ru',
#     'overembed': 'false',
#     'ncrnd': '0.23800355071570123',
# }
# response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, headers=headers)
# chart = response.json()['chartPositions']
# for track in chart:
#     position = track['track']['chart']['position']
#     title = track['track']['title']
#     author = track['track']['artists'][0]['name']
#     data = response.json() 
#     with open("data.json", "w") as f:            
#             json.dump(data, f, ensure_ascii=False)
#     print(f"N-{position} - {author} - {title}")
    