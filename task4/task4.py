from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

PATH_TO_DRIVER = '../chromedriver.exe'
WORD = "hug"

def synonym(word, driver_path):

    URL = "https://www.thesaurus.com/browse/" + word

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    driver.get(URL)

    xpath = "//section[starts-with(@class, 'synonyms-container')]/ul/li/span/a"
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
    )

    synonym = driver.find_element_by_xpath(xpath).text

    driver.quit()

    return synonym

if __name__ == "__main__":
    print(synonym(WORD, PATH_TO_DRIVER))