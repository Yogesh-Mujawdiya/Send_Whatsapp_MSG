from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# list of number with country code without '+' sign
Contacts = []
Message = 'testing whatsapp MSG'
with open('numlist.txt', 'r') as contacts:
    for line in contacts.readlines():
        line = line.rstrip()
        Contacts.append(line)

driver = webdriver.Chrome(executable_path="chromedriver")
driver.set_page_load_timeout(60 * 5)  # for slow internet

print('starting')
for Contact in Contacts:
    print("sending msg to {}".format(Contact))
    driver.get("http://web.whatsapp.com/send?phone={}&text={}"
               .format(Contact, Message))
    wait = WebDriverWait(driver, 1000)
    # get send arrow and click it
    sendbtn_xpath = '//span[@data-icon="send"]'
    sendbtn = wait.until(EC.presence_of_element_located((By.XPATH, sendbtn_xpath)))
    sendbtn.click()
    # wait until message is sent
    msg_time_xpath = '//span[@data-icon="msg-time"]'
    msg_sent = wait.until(EC.invisibility_of_element_located((By.XPATH, msg_time_xpath)))

print('ending')
driver.close()
