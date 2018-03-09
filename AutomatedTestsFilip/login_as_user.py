from selenium import webdriver
from time import sleep

# the purpose of this automated test case is to verify that is possible to login as a user

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://demo.fluxday.io/users/sign_in')
browser.find_element_by_xpath('//*[@id="user_email"]').send_keys('emp1@fluxday.io')
browser.find_element_by_xpath('//*[@id="user_password"]').send_keys('password')
browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/button').click()
login_alert = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div')
user = browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul[3]/li[1]/a')
employee1 = "Employee 1"

assert login_alert == browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div'), \
    'Problem with login alert bottom right'
assert user.text == employee1, 'Login user is not the same'

sleep(3)
browser.close()
