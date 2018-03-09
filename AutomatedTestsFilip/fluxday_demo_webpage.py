from selenium import webdriver
from time import sleep

"""
The purpose of this automated test case is to check if it is possible to open fluxday demo web page
"""

xp_expr_demo_webpage = '//*[@id="new_user"]'
xp_expr_email_textbox = '//*[@id="user_email"]'
xp_expr_password_textbox = '//*[@id="user_password"]'
xp_expr_login_btn = '//*[@id="new_user"]/div[2]/div[3]/button'
xp_expr_logo = '//*[@id="page-top"]/nav/div/div[1]/a/img[1]'
xp_expr_active_demo = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]'


browser = webdriver.Chrome()
browser.maximize_window()
# Opens website homepage (http://fluxday.io)
browser.get('http://fluxday.io')
logo = browser.find_element_by_xpath(xp_expr_logo)
assert logo == browser.find_element_by_xpath(xp_expr_logo), 'logo is not the same'
# Click on 'demo' from the top menu
browser.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]/a').click()
sleep(2)
active_demo = browser.find_element_by_xpath(xp_expr_active_demo)
assert 'active' in active_demo.get_attribute('class'), 'logo is not the same'
# Click on 'Try Live Demo'
browser.find_element_by_xpath('//*[@id="help"]/div/div[2]/div/div[3]/a').click()
# Closing current browser
browser.close()
# Saves id of the new browser
window_after = browser.window_handles[0]
# Switching to the newly opened browser
browser.switch_to.window(window_after)

demo_webpage = browser.find_element_by_xpath(xp_expr_demo_webpage)
assert demo_webpage == browser.find_element_by_xpath(xp_expr_demo_webpage), 'problem with new user form '

email_textbox = browser.find_element_by_xpath(xp_expr_email_textbox)
assert email_textbox == browser.find_element_by_xpath(xp_expr_email_textbox), 'problem with email textbox'

password_textbox = browser.find_element_by_xpath(xp_expr_password_textbox)
assert password_textbox == browser.find_element_by_xpath(xp_expr_password_textbox), 'problem with password textbox'

login_btn = browser.find_element_by_xpath(xp_expr_login_btn)
assert login_btn == browser.find_element_by_xpath(xp_expr_login_btn), 'problem with login btn'

sleep(3)
browser.close()
