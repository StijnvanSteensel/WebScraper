import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def Scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path = "./Chromedriver.exe"
    Options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=Options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

