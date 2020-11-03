from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# tell selenium what website to go to
DRIVER_PATH = '/Users/GrantRudow/Documents/YouTubeProjects/chromedriver'

# opens the chrome window
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.imleagues.com/spa/fitness/ea730a742e724737b23ae8a45efd572c/home')

# tell chrome not to open, but run on the server
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get('https://www.imleagues.com/spa/fitness/ea730a742e724737b23ae8a45efd572c/home')

# tell selenium to wait for the page to load before clicking button
wait = WebDriverWait(driver, 100)

# wait for page to load
time.sleep(6)
# click next button to go to next day
nextButton = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/button[2]/span")
nextButton.click()

# find the correct zone and time
time.sleep(3)
zone = driver.find_element_by_xpath("//*[text()='Zone 2: 1st Floor Strength/Turf')]")

zone.click()


time.sleep(15)
driver.quit()









