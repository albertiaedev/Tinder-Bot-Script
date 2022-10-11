from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Download ChromeDriver at: https://chromedriver.chromium.org/downloads

# Remember you need to run Google Chrome on debugging mode

path = # 'insert here the path of chromedriver in your computer'
service = Service(executable_path=path)
web = 'https://www.tinder.com/'

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:#')
driver = webdriver.Chrome(service=service, options=opt)
