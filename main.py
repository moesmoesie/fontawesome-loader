from asyncio import constants
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Safari()

url = "https://fontawesome.com/search?"
full_data = []


for type in ["solid","brands"]:
    currentPage = 1
    while True:
        params = {"m" : "free","p" : currentPage, "s":type}
        fullUrl = url + urllib.parse.urlencode(params)
        driver.get(fullUrl)
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.CLASS_NAME, "wrap-icon")
        currentPage += 1

        if len(elements) == 0:
            break;

        print

        for element in elements:
            identifier = element.get_attribute("id")
            values = identifier.split("-")
            name = "-".join(values[1:-1])
            data = {
                "name" : name + " " + values[-1],
                "value" : name + "@" + values[-1]
            }
            full_data.append(data)

d = json.dumps(full_data)
with open('fontawesome.json', 'w') as f:
    json.dump(d, f)