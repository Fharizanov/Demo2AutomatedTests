from selenium import webdriver
from time import sleep

'''
The purpose of this automated test case is to show on the screen the team lead profile while logged in as user
'''

xp_expr_demo_webpage = '//*[@id="new_user"]'
xp_expr_email_textbox = '//*[@id="user_email"]'
xp_expr_password_textbox = '//*[@id="user_password"]'
xp_expr_login_btn = '//*[@id="new_user"]/div[2]/div[3]/button'
xp_expr_login_alert = '/html/body/div[2]/div[1]/div/div'
xp_expr_user_name = '/html/body/div[2]/div[1]/ul[3]/li[1]/a'
xp_expr_users_btn = '/html/body/div[2]/div[1]/ul[2]/li[5]/a'
xp_expr_users = '//*[@id="pane2"]/div[2]/div'
xp_expr_lead = '//*[@id="pane2"]/div[2]/div[4]/div/div[2]/a[1]'
xp_expr_lead_rights = '//*[@id="pane3"]/div/div[1]/div[1]'
xp_expr_lead_reporting_to = '//*[@id="pane3"]/div/div[1]/div[6]/a'

name = 'emp1@fluxday.io'
password = 'password'
employee1 = "Employee 1"


browser = webdriver.Chrome()
browser.maximize_window()
# Opens website demo homepage (http://demo.fluxday.io/users/sign_in)
browser.get('http://demo.fluxday.io/users/sign_in')
demo_webpage = browser.find_element_by_xpath(xp_expr_demo_webpage)
assert demo_webpage == browser.find_element_by_xpath(xp_expr_demo_webpage), 'Problem with new user form'
# Checks if there is an email textbox and enters the email of the current user
browser.find_element_by_xpath(xp_expr_email_textbox).send_keys(name)
email_textbox = browser.find_element_by_xpath(xp_expr_email_textbox)
assert email_textbox == browser.find_element_by_xpath(xp_expr_email_textbox), 'Problem with email textbox'
# Checks if there is a password textbox and enters the password of the current user
browser.find_element_by_xpath(xp_expr_password_textbox).send_keys(password)
password_textbox = browser.find_element_by_xpath(xp_expr_password_textbox)
assert password_textbox == browser.find_element_by_xpath(xp_expr_password_textbox), 'Problem with password textbox'
# Checks if there is a login button
browser.find_element_by_xpath(xp_expr_login_btn)
login_btn = browser.find_element_by_xpath(xp_expr_login_btn)
assert login_btn == browser.find_element_by_xpath(xp_expr_login_btn), 'Problem with login button'
# Checks if there is a login button and clicks on it
browser.find_element_by_xpath(xp_expr_login_btn).click()
# Checks if there is a login alert which assures that a login was successful
login_alert = browser.find_element_by_xpath(xp_expr_login_alert)
assert login_alert == browser.find_element_by_xpath(xp_expr_login_alert), 'Problem with login alert bottom right'
# Checks if the logged user is Employee 1
user = browser.find_element_by_xpath(xp_expr_user_name)
assert user.text == employee1, 'Login user is not the same'
sleep(1)
# Clicks on 'Users' button on the left side of the screen
browser.find_element_by_xpath(xp_expr_users_btn).click()
sleep(1)
users = browser.find_elements_by_xpath(xp_expr_users)
assert len(users) != 0, "There are no users"
assert len(users) > 0, "Problem with users counting"
# Clicks on 'Team Lead' user
browser.find_element_by_xpath(xp_expr_lead).click()
sleep(1)
lead_rights = browser.find_element_by_xpath(xp_expr_lead_rights)
assert lead_rights.text == '#FT2', "Problem with opened profile. Team lead rights do not match."
lead_reporting_to = browser.find_element_by_xpath(xp_expr_lead_reporting_to)
assert lead_reporting_to.text == 'Admin User', "Problem with team lead reporting managers." \
                                               " Admin User reference do not match."

sleep(2)
# Closing current browser
browser.close()
