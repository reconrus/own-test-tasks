from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

URL = "https://stackoverflow.com/questions/3044620/python-vs-java-performance-runtime-speed"
PATH_TO_DRIVER = '../chromedriver.exe'

def mentioned_users(url, driver_path):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    driver.get(URL)
    actions = ActionChains(driver)

    try:
        notice_close = driver.find_element_by_css_selector(".grid--cell.fc-white.js-notice-close")
        notice_close.click()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".grid--cell.fc-white.js-notice-close"))
        )
    except:
        pass

    comments = driver.find_elements_by_xpath("//a[starts-with(text(),'show ')]")

    for comment in comments:    
        actions.move_to_element(comment).click().perform()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(comment)
        )

    soup = BeautifulSoup(driver.page_source, features='html.parser')
    driver.quit()

    users = []

    comments = soup.findAll("a", href=re.compile("/users/(\d+)/*"), text=True)

    for comment in comments:
        users.append(comment.getText())

    return sorted(set(users), key=lambda x: x.capitalize())


if __name__ == "__main__":
    print(mentioned_users(URL, PATH_TO_DRIVER))