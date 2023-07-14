import io, time, bs4
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getChampStats(numChamps):
    champStats = np.zeros((numChamps, 2, 1)) 
    #TODO: ^^^8 is for num stats, currently 1 for development
    #The 2 is for 2 levels, lvl 1 and lvl 18
    champCounter = 0
    driver = webdriver.Chrome()
    champListUrl = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
    driver.get(champListUrl)
    selectedElement = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    selectedElement.click() #close notification tab

    #Finds champion table
    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr") 
    for tr in selElement0:
        if champCounter == numChamps: break
        #Find champion page link
        time.sleep(0.2)
        selectedElement = (tr.find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "span").
                    find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a"))
        link = selectedElement.get_attribute("href")
        print(link)
        
        #Need to recreate a new driver, or else using website navigation will leave "selElement" stale
        #TODO: Could probably open link in a new window or tab, probably be more efficient? IDK still works without
        tempDriver = webdriver.Chrome()
        tempDriver.get(link)
        print(tempDriver.find_element(By.TAG_NAME, "head").find_element(By.TAG_NAME, "title").get_attribute("innerText"))
        print(tempDriver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[8]').get_dom_attribute("class"))

        #TODO: Add more data, this is just for health
        data = (tempDriver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[8]/aside/section[1]/section[1]/section/div[1]').
                find_elements(By.TAG_NAME, "span")[1].get_attribute("innerText"))
        #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1].get_dom_attribute("class")
        #^^^ this is the original xPath, however does not work, idk why div[8] is needed and not div[9]... indexing seems
        #like the problem, inconsistant. https://www.w3schools.com/xml/xpath_syntax.asp
        
        #TODO: VV make more generalizable for more stats
        data = data.rsplit(sep=" – ")
        champStats[champCounter][0][0] = int(data[0]) 
        champStats[champCounter][1][0] = int(data[1]) 

        tempDriver.quit()
        champCounter += 1
    
    driver.quit()
    return champStats
    
print(getChampStats(4))


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