"""
The purpose of this automated test case is to show on the screen the completed tasks
"""

from selenium import webdriver
from time import sleep

xp_expr_demo_webpage = '//*[@id="new_user"]'
xp_expr_email_textbox = '//*[@id="user_email"]'
xp_expr_password_textbox = '//*[@id="user_password"]'
xp_expr_login_btn = '//*[@id="new_user"]/div[2]/div[3]/button'
xp_expr_login_alert = '/html/body/div[2]/div[1]/div/div'
xp_expr_user_name = '/html/body/div[2]/div[1]/ul[3]/li[1]/a'
xp_expr_tasks = '/html/body/div[2]/div[1]/ul[2]/li[2]/a'
xp_expr_pending_btn = '//*[@id="pane2"]/div[1]/dl/dd[1]'
xp_expr_completed_btn = '//*[@id="pane2"]/div[1]/dl/dd[2]/a'
xp_expr_completed_active_btn = '//*[@id="pane2"]/div[1]/dl/dd[2]'
xp_expr_completed_tasks = '//*[@id="paginator"]/a'

name = 'emp1@fluxday.io'
password = 'password'
employee1 = "Employee 1"


browser = webdriver.Chrome()
browser.maximize_window()

# Opens website demo homepage (http://demo.fluxday.io/users/sign_in)
browser.get('http://demo.fluxday.io/users/sign_in')
demo_web_page = browser.find_element_by_xpath(xp_expr_demo_webpage)
assert demo_web_page == browser.find_element_by_xpath(xp_expr_demo_webpage), 'Problem with new user form'

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

# Checks if there is a My tasks button and clicks on it
browser.find_element_by_xpath(xp_expr_tasks).click()
sleep(1)
active_pending = browser.find_element_by_xpath(xp_expr_pending_btn)
assert 'active' in active_pending.get_attribute('class'), 'Button Pending is not active'

# Checks if there is a Completed button and clicks on it
browser.find_element_by_xpath(xp_expr_completed_btn).click()
active_completed = browser.find_element_by_xpath(xp_expr_completed_active_btn)
assert 'active' in active_completed.get_attribute('class'), 'Button Completed is not active'

# Checks if there are any completed tasks
completed_tasks = browser.find_elements_by_xpath(xp_expr_completed_tasks)
assert len(completed_tasks) != 0, "There are no completed tasks"
assert len(completed_tasks) > 0, "Problem with completed tasks"

sleep(1)
# Closing current browser
browser.close()
