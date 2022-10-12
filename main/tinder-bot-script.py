from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Download ChromeDriver at: https://chromedriver.chromium.org/downloads

# Remember you need to run Google Chrome on debugging mode

path = # 'insert here the path of chromedriver in your computer'
service = Service(executable_path=path)
web = 'https://www.tinder.com/'

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:#')
driver = webdriver.Chrome(service=service, options=opt)

driver.get(web)

# automate 'swipe right'
like = driver.find_element(by='xpath', value='//button//span[text()="Like"]')
driver.execute_script("argument[0].click();", like)
time.sleep(2)

# automate a match message
match = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice!"]')
#you may need to change the placeholder to your local language
hook = "They say love is important, but I think YOU are more important" #yes, it's cheesy. Don't blame me lol
match.send_keys(hook)

send = driver.find_element(by='xpath', value='//button/span[text()="Send"]')
send.click()
time.sleep(1)

close = driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
close.click()
