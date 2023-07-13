import io, time
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def getChampStats(numChamps):
    champStats = np.zeros((numChamps, 8)) #8 is for num stats
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    element0 = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    element0.click()

    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr")
    for tr in selElement0:
        element0 = (tr.find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "span").
                    find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a"))
        print(element0.screenshot_as_png)
        print(element0.text)
        time.sleep(5)
        element0.click()
        element1 = (driver.find_element(By.CLASS_NAME, "pi-item pi-group pi-border-color").
                    find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "span")[1])
        print(element1.text)
        #for i in range(8):

    
    
    driver.quit()

getChampStats(4)

def test():
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    element0 = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    element0.click()

    element1 = driver.find_element(By.CLASS_NAME, "mw-redirect")
    print(element1.text)
    element1.click()
    
    print(driver.current_url)



def getChampList():
    champList = []
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr")
    for tr in selElement0:
        selElement1 = tr.find_element(By.TAG_NAME, "td")
        attrStr =  selElement1.get_attribute("data-sort-value")
        champList.append(attrStr)
        
    driver.quit()
    #print(tuple(champList))
    return(tuple(champList))

#getChampList()