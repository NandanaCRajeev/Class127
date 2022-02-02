from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver_win32\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrap():
    headers=["name","light_years_from_earth","planet_mars","stellar_magnitude","discovery_date"]
    planet_data=[]
    for i in range (0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","expo planets"}):
            li_tags=ul_tag.find_all ("li")
            temp_list=[]
            for index,li_tags in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_Xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w") as f:
        csvwritter=csv.writer(f)
        csvwritter.writerow(headers)
        csvwritter.writerows(planet_data)
scrap()

