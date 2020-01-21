from selenium import webdriver
from selenium.webdriver.chrome.options import Options
c_options = Options()
c_options.add_argument("--headless")
b = webdriver.Chrome(options=c_options)
b.get('https://twins.tsukuba.ac.jp/campusweb/campusportal.do')
print(b.page_source)
b.close()
