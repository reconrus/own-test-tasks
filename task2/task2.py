from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

PATH_TO_DRIVER = 'chromedriver.exe'
CITIES = ["Kazan", "Moscow", "London"]

def weather(cities, driver_path):

    URL = "https://yandex.com/weather/"
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    JSON = {
        "weatherData": []
    }
    
    for city in cities:
        driver.get(URL+city)

        WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".temp.fact__temp.fact__temp_size_s"))
        )

        weather_element = driver.find_element_by_xpath("//span[contains(@class, 'temp__value')]/ancestor::div[contains(@class, 'temp fact__temp fact__temp_size_s')]")
        weather = (-1)*int(weather_element.text[1:-1]) if weather_element.text[0] == '−' else int(weather_element.text[:-1]) 
        JSON["weatherData"].append({"cityName":city, "degreesCelsius": weather})
    
    driver.quit()

    with open('result.json', 'w') as fp:
        json.dump(JSON, fp)

    return JSON

if __name__ == "__main__":
    print(weather(CITIES, PATH_TO_DRIVER))