from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.iottechnews.com/")


source_file = open("sel.html","w")
html = driver.page_source
soup = BeautifulSoup(html ,'lxml')
source_file.write(soup.prettify())


driver.close()