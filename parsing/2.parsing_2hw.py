import requests
from bs4 import BeautifulSoup
import time
import json


cookies = {
    'PHPSESSID': 'p02kf709sm0thf9jfuj03tfcmt',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga': 'GA1.1.2058913975.1696945828',
    '_ym_uid': '1696945829221031195',
    '_ym_d': '1696945829',
    '_ym_isad': '1',
    '_ga_BB3QC8QLF4': 'GS1.1.1696945827.1.1.1696946151.0.0.0',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=p02kf709sm0thf9jfuj03tfcmt; 51a55dae53577255b792d39bfe1d40ac=1; _ga=GA1.1.2058913975.1696945828; _ym_uid=1696945829221031195; _ym_d=1696945829; _ym_isad=1; _ga_BB3QC8QLF4=GS1.1.1696945827.1.1.1696946151.0.0.0',
    'dnt': '1',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

games = {}
for i in range(1, 3):
    params = {
        'p': str(i),
    }
    time.sleep(1)
    print(f'собираю данные со страницы {i}')
    response = requests.get('https://zaka-zaka.com/game/new/', cookies=cookies, headers=headers)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        # container = soup.find("div",class_="mainpage-catalog")
        cards = soup.find_all("div",class_="game-block")
        for card in cards:
            if "game-block-more" in card.get("class"):
                continue
            name = card.find("div",class_ = "game-block-name").text.strip()
            price = card.find("div",class_="game-block-prices").text.strip()[:7]
            games[name.text]=price.text

with open("data.json", "w") as file:
    json.dump(games, file)
print(games)
