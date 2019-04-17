from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


PATH_TO_DRIVER = '../chromedriver.exe'
KEYWORDS = "python qt"

def popular_repositories(keywords, driver_path):

    URL = "https://github.com/search?q=" + '+'.join(keywords.split())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    driver.get(URL)

    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@data-hydro-click, '\"result_position\":10')]"))
    )

    links = []

    repos = driver.find_elements_by_xpath("//a[contains(@data-hydro-click, '\"result_position\"')]")
    
    for i in range(5): 
        links.append(repos[i].get_attribute("href"))

    driver.quit()

    return links

if __name__ == "__main__":
    print(popular_repositories(KEYWORDS, PATH_TO_DRIVER))