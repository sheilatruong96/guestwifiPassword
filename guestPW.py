from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("/home/opc/project/chromedriver", options=options)

driver.get("https://myaccess.oraclevpn.com")
usernameElement = driver.find_element_by_id("username")
usernameElement.send_keys("<username>")

passwordElement = driver.find_element_by_id("password_input")
passwordElement.send_keys("<password>")

passwordElement.submit()

https = Select(driver.find_element_by_id('protocol_selector'))
https.select_by_value('https://')

url = driver.find_element_by_id('unicorn_form_url')
url.send_keys("https://gmp.oracle.com/captcha/fi1es/amer.txt?_dc=1575486564313")
url.submit()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sso_username")))
    usernameElement = driver.find_element_by_id("sso_username")
    usernameElement.send_keys("<email>")

    passwordElement = driver.find_element_by_id("ssopassword")
    passwordElement.send_keys("<password>")
    passwordElement.submit()
finally:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    print(soup.pre.string)
    driver.quit()

