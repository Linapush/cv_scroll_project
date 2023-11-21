from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
from time import sleep
from json import dump

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)

driver.get("https://store.steampowered.com/")
search_form = driver.find_element(by="id", value="store_nav_search_term")
search_form.send_keys("Стратегии")
search_form.send_keys(Keys.ENTER)
sleep(3)
for i in range(15):
    driver.execute_script("window.scrollBy(0, 1080)")
    sleep(0.5)

page = driver.page_source
soup = BeautifulSoup(page, "lxml")
container = soup.find_all("div", class_ = "responsive_search_name_combined")

result = {}
for card in container:
    title = card.find("span", class_="title").text
    price = card.find("div", class_="discount_final_price")
    if price:
        result[title] = price.text

with open("result.json", "w") as f:
    dump(result,f,ensure_ascii=False)
