from selenium import webdriver

DRIVER_PATH = '/Users/GrantRudow/Documents/YouTubeProjects/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')
