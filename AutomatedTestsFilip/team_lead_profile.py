from selenium import webdriver
from time import sleep

# the purpose of this automated test case is to show on the screen the team lead profile while logged in as user

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://demo.fluxday.io/users/sign_in')
browser.find_element_by_xpath('//*[@id="user_email"]').send_keys('emp1@fluxday.io')
browser.find_element_by_xpath('//*[@id="user_password"]').send_keys('password')
browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/button').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[5]/a').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="pane2"]/div[2]/div[4]/div/div[2]/a[1]').click()
sleep(1)
lead_rights = browser.find_element_by_xpath('//*[@id="pane3"]/div/div[1]/div[1]')
lead_reporting_to = browser.find_element_by_xpath('//*[@id="pane3"]/div/div[1]/div[6]/a')
sleep(1)

# print(lead_rights.text)
# print(lead_reporting_to.text)
assert lead_rights.text == '#FT2', "Problem with opened profile. Team lead rights do not match."
assert lead_reporting_to.text == 'Admin User', "Problem with team lead reporting managers. Admin User ref do not match."
sleep(2)
browser.close()
