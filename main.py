import io
import numpy as np
import requests, selenium, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def bs():
    #url = "https://www.google.com/" 
    url = "https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol"

    r = requests.get(url)
    #print(r.headers)
    #print(r.text)

    soup = bs4.BeautifulSoup(r.content, features="html.parser")
    output = soup.find_all('bg-quote', class_ = "value")
    for x in output:
        print(x)
    print(output[0].text)

def simpleExample():
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/Aatrox/LoL")
    selectedElement = driver.find_element(By.ID, "lvl_Aatrox")
    select = Select(selectedElement).select_by_index(3)
    selectedElement = driver.find_element(By.ID, "AttackDamage_Aatrox_lvl")
    print(selectedElement.text)
    driver.quit()

simpleExample()

