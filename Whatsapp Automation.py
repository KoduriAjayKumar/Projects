#Whatsapp Automation using Selenium library
#In this project we send 100 messages to a friend who is in our contact list using Selenium library.
#Note: For selenium library we need to download chorme web dirver or any other web driver and webdriver should be kept in c drive in windows folder for windows operating system.



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://whatsapp.com")
driver.maximize_window()
element = driver.find_element_by_link_text("WHATSAPP WEB")
element.click()
time.sleep(3)

wait = WebDriverWait(driver, 600)
target = '"Amma ❣️"' #Enter your friend name in your contact list to send message.
message = "Hello, this message sent using python." #Enter the message that you need to sent.

x_arg = '//span[contains(@title, '+target+')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

time.sleep(2)
input_box = driver.find_element_by_class_name("p3_M1")
for i in range(10):
    input_box.send_keys(message+Keys.ENTER)