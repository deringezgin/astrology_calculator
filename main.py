### Import Statements ###
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import calendar
import time


def fill_form(item):
    actions.send_keys(item, Keys.TAB)
    actions.perform()

# Website Link
astrology_link = "https://www.astrologicalassociation.com/chart-calculator/"

name = input("Please enter your name: ")

DD_MM_YYYY = input("Please enter your birthday as DD-MM-YYYY (07-11-2004): ")
date = DD_MM_YYYY.split("-")
day = int(date[0])
month = calendar.month_name[int(date[1])]
year = date[2]

HH_MM = input("Please enter your birth time as HH.MM (20.10): ")
hour_min = HH_MM.split(".")
hour = hour_min[0]
min = hour_min[1]

city = "Izmir"

service = Service("/Users/deringezgin/Documents/deringezgin/CS Books/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(astrology_link)
driver.maximize_window()
actions = ActionChains(driver)

name_field = driver.find_element(by=By.ID, value="name")
name_field.click()

elements = [name, month, day, year, hour, min]

# Filling the website
for element in elements:
    fill_form(element)

actions.send_keys(Keys.TAB, city)
actions.perform()
time.sleep(5)

actions.send_keys(Keys.DOWN, Keys.ENTER)
actions.perform()
time.sleep(3)

actions.send_keys(Keys.TAB, Keys.ENTER)
actions.perform()
time.sleep(5)

planets = []
for i in range(1, 12):
    planet = driver.find_element(by=By.XPATH, value=f'//*[@id="zp-report-content"]/p[{i}]')
    planets.append(planet.text)

planets = [(" ".join((planet.split(" "))[:3])) for planet in planets]

houses = []
for i in range(17, 100):
    house = driver.find_element(by=By.XPATH, value=f'//*[@id="zp-report-content"]/p[{i}]')
    if house.text[:5] == "Pluto":
        houses.append(house.text)
        break
    else:
        houses.append(house.text)

new_houses = []
for house in houses:
    if house[:4] != "NOTE":
        house = (" ".join((house.split(" "))[:4]))
        new_houses.append(house)
    else:
        new_houses.append(house)

print("\n")
for planet in planets:
    print(planet)

print("\n")
for house in houses:
    print(house)
