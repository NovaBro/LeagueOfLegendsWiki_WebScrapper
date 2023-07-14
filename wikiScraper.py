import io, time
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def getChampStats(numChamps):
    champStats = np.zeros((numChamps, 8)) #8 is for num stats
    driver = webdriver.Chrome()
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    originalWeb = driver.current_window_handle
    selectedElement = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    selectedElement.click()

    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr")
    for tr in selElement0:
        #Click on champion page link
        selectedElement = (tr.find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "span").
                    find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a"))
        link = selectedElement.get_attribute("href")
        print(link)

        """ scrollPoint = ScrollOrigin.from_element(selectedElement)
        time.sleep(5)
        ActionChains(driver).scroll_from_origin(scrollPoint, 0, 0).perform() """
        """ ActionChains(driver)\
        .scroll_by_amount(0, 1000)\
        .perform()
        time.sleep(0.25)
        selectedElement.click()
        time.sleep(0.25) """


        tempDriver = webdriver.Chrome()
        tempDriver.get(f"{link}")
        #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1]
        #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1]
        #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section
        #//*[@id="mw-content-text"]/div[1]/div[8]/aside/section[1]/section[1]/section/div[1]
        #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[9]/aside/section[1]/section[1]/section
        #/html/body/div[4]/div[4]/div[3]/main/div[3]/div[2]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1]
        #/html/body/div[4]/div[4]/div[2]/main/div[3]/div[2]/div[1]/div[8]/aside/section[1]/section[1]/section/div[1]
        time.sleep(1)
        
        healthRange = tempDriver.find_element(By.CSS_SELECTOR, 'data-source="health"').\
            find_elements(By.TAG_NAME, "span")[1].text
        print(healthRange)
        tempDriver.quit()


        """ selectedElement = driver.find_element(By.CLASS_NAME, "lvlselect lvlselect-initialized").\
                    find_element(By.TAG_NAME, "aside").\
                    find_element(By.CLASS_NAME, "pi-item pi-group pi-border-color")
                    #.find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "span")[1])
        print(selectedElement.text) """
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