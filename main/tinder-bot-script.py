from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Download ChromeDriver at: https://chromedriver.chromium.org/downloads

path = # 'insert here the path of chromedriver in your computer'
service = Service(executable_path=path)
web = 'https://www.tinder.com/'
driver = webdriver.Chrome(service=service)
