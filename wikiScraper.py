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

op = webdriver.ChromeOptions()
op.add_argument('headless')
numStats = 7

def getSpecChampStats(champName:str):
    #The 18 is for 18 levels, 1 is for the number of stats
    champStats = np.zeros((18, numStats)) 

    driver = webdriver.Chrome(options=op)
    champListUrl = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
    driver.get(champListUrl)

    selectedElement = (driver.find_element(By.CLASS_NAME, "sitenotice-wrapper__header")
                .find_element(By.TAG_NAME, "svg").find_element(By.TAG_NAME, "use"))
    selectedElement.click()#close notification tabf

    #Finds champion table
    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").\
        find_element(By.CSS_SELECTOR, f"[data-sort-value='{champName}']")
    champURL = selElement0.find_element(By.TAG_NAME, "span").\
        find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a").get_attribute("href")
    
    #Need to recreate a new driver, or else using website navigation will leave "selElement" stale
    #TODO: Could probably open link in a new window or tab, probably be more efficient? IDK still works without
    tempDriver = webdriver.Chrome(options=op)
    tempDriver.get(champURL)
    print(champURL)

    #Grabs the select option of champion stats
    #XPATH: #mw-content-text > div.mw-parser-output > div.lvlselect.lvlselect-initialized > aside > h2 > div
    selElement1 = tempDriver.find_element(By.CSS_SELECTOR, "#mw-content-text").find_element(By.CSS_SELECTOR, "div.mw-parser-output").\
                    find_element(By.CSS_SELECTOR, "div.lvlselect.lvlselect-initialized").find_element(By.CSS_SELECTOR, "aside").\
                    find_element(By.CSS_SELECTOR, "h2").find_element(By.CSS_SELECTOR, "div").\
                    find_element(By.TAG_NAME, "select")

    for lvl in range(2, 20): #LVL range
        selectOpt = Select(selElement1)
        selectOpt.select_by_index(lvl)
        data = np.zeros((numStats))
        
        #This loops iteratees through some of the stats of the champion
        #There is this weird loop cause I do not want to collect all the data, since the HTML structure is not uniform
        runLoop = True
        for s in range(5): 
            if not runLoop: break
            for d in range(2):
                if s == 3 and d == 1 : 
                    runLoop = False
                    break
                #print(s,"||", d)
                try:
                    colectedData = tempDriver.find_element(By.CSS_SELECTOR, "#mw-content-text").find_element(By.CSS_SELECTOR, "div.mw-parser-output").\
                        find_element(By.CSS_SELECTOR, "div.lvlselect.lvlselect-initialized").find_element(By.CSS_SELECTOR, "aside").\
                        find_element(By.CSS_SELECTOR, "section:nth-child(2)").find_element(By.CSS_SELECTOR, f"section:nth-child({(s+1)})").\
                        find_element(By.TAG_NAME, "section").find_element(By.CSS_SELECTOR, f"div:nth-child({(d+1)})").\
                        find_elements(By.TAG_NAME, "span")[1].get_attribute("innerText")
                #//*[@id="mw-content-text"]/div[1]/div[9]/aside/section[1]/section[1]/section/div[1].get_dom_attribute("class")
                #^^^ this is the original xPath, however does not work, idk why div[8] is needed and not div[9]... indexing seems
                #like the problem, inconsistant. https://www.w3schools.com/xml/xpath_syntax.asp
                except:
                    colectedData = tempDriver.find_element(By.CSS_SELECTOR, "#mw-content-text").find_element(By.CSS_SELECTOR, "div.mw-parser-output").\
                        find_element(By.CSS_SELECTOR, "div.lvlselect.lvlselect-initialized").find_element(By.CSS_SELECTOR, "aside").\
                        find_element(By.CSS_SELECTOR, "section:nth-child(2)").find_element(By.CSS_SELECTOR, f"section:nth-child({(s+1)})").\
                        find_element(By.TAG_NAME, "section").find_element(By.CSS_SELECTOR, f"div:nth-child({(d+1)})").\
                        get_dom_attribute("innerText")#get_attribute("innerText")

                if colectedData == "N/A" or colectedData == "" or colectedData == None: colectedData = 0
                data[(s * 2 + d)] = (colectedData)
        
        champStats[lvl - 2] = (data)

    tempDriver.quit()
    driver.quit()
    return champStats

def getChampList():
    champList = []
    driver = webdriver.Chrome(options=op)
    driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    selElement0 = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/table/tbody").find_elements(By.TAG_NAME, "tr")
    for tr in selElement0:
        selElement1 = tr.find_element(By.TAG_NAME, "td")
        attrStr =  selElement1.get_attribute("data-sort-value")
        champList.append(attrStr)
        
    driver.quit()
    return(tuple(champList))
