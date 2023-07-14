import io, time
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


def getChampStats(numChamps):
    champStats = np.zeros((numChamps, 8)) #8 is for num stats
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    selectedElement = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    selectedElement.click() #close notification tab

    #Finds champion table
    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr") 
    for tr in selElement0:
        #Click on champion page link
        selectedElement = (tr.find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "span").
                    find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a"))
        link = selectedElement.get_attribute("href")
        print(link)

        #TODO: USE REAL WEBSITE SELENIUM METHODS
        #Champion Page
        tempDriver = webdriver.Chrome()
        tempDriver.get(f"{link}")
        time.sleep(1)

        #//*[@id="mw-content-text"]/div[1]/div[9]
        print(tempDriver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[3]/div[2]/span').text)
        #print(tempDriver.find_element(By.XPATH, '/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[3]/div[2]/span').text)
        time.sleep(10)
        healthRange = tempDriver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[9]').find_elements(By.XPATH, '*')
        print(tempDriver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]').get_attribute("class"))
            #TODO:for Loop for rest of stats, just starting with health
            #SHOULD BE ABLE TO FIND: //*[@id="mw-content-text"]/div[1]/div[9]
            #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1]
            #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1]
        print(healthRange)
        tempDriver.quit()
    
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