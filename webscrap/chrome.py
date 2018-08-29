from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")


# options = Options()
# options.set_headless(headless=True)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.set_page_load_timeout(50)
# driver.set_script_timeout(3)



try:
    driver.get("https://www.iottechnews.com/")
except TimeoutException:
    driver.execute_script("window.stop();")



source_file = open("selenium_iot_withtimeout_soup.html","w")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

source_file.write(soup.prettify())


driver.close()