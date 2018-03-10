from selenium import webdriver
from time import sleep

'''
The purpose of this automated test case is to verify it is possible to write a comment for a task
'''

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
xp_expr_first_completed_task = '//*[@id="paginator"]/a[1]/div'
xp_expr_comments_num = '//*[@id="pane3"]/div[2]/div/div[2]/a'
xp_expr_comments = '//*[@id="pane3"]/div[2]/div/div[2]/div'
xp_expr_comments_textbox = '//*[@id="comment_body"]'

name = 'emp1@fluxday.io'
password = 'password'
employee1 = "Employee 1"
comment = 'Test comment 1'

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
# Checks if there is a My tasks button and clicks on it
browser.find_element_by_xpath(xp_expr_tasks).click()
sleep(1)
active_pending = browser.find_element_by_xpath(xp_expr_pending_btn)
assert 'active' in active_pending.get_attribute('class'), 'Button Pending is not active'
sleep(1)
# Checks if there is a Completed button and clicks on it
browser.find_element_by_xpath(xp_expr_completed_btn).click()
sleep(1)
active_completed = browser.find_element_by_xpath(xp_expr_completed_active_btn)
assert 'active' in active_completed.get_attribute('class'), 'Button Completed is not active'
sleep(1)
# Checks if there are any completed tasks
completed_tasks = browser.find_elements_by_xpath(xp_expr_completed_tasks)
assert len(completed_tasks) != 0, "There are no completed tasks"
assert len(completed_tasks) > 0, "Problem with completed tasks"
# Clicks on the first completed task from the top
browser.find_element_by_xpath(xp_expr_first_completed_task).click()
sleep(1)
active_first_task = browser.find_element_by_xpath(xp_expr_first_completed_task)
assert 'active' in active_first_task.get_attribute('class'), 'Clicking on first task is not active'
# Click on the number of comments (under 'Add comment' textbox) to show them if any
browser.find_element_by_xpath(xp_expr_comments_num).click()
sleep(1)
# Saves the number of comments before submitting new
comments_before = browser.find_elements_by_xpath(xp_expr_comments)
# Checks if there is a 'Add comment' textbox and enters the desired keys
browser.find_element_by_xpath(xp_expr_comments_textbox).send_keys(comment)
# Submits the desired keys as a comment
browser.find_element_by_xpath(xp_expr_comments_textbox).submit()
sleep(1)
# Verifies that a comment 'Test comment 1" is submited
comments_number = browser.find_elements_by_xpath(xp_expr_comments)
test_comm = browser.find_element_by_xpath('//*[@id="pane3"]/div[2]/div/div[2]/div[' + str(len(comments_number)) + ']')
assert test_comm.text == ('emp1 Just now' + comment) or ('emp1 1 second ago' + comment), 'Submitted comment - different'
sleep(1)
# Saves comments number after submitting new
comments_after = browser.find_elements_by_xpath(xp_expr_comments)
sleep(1)
# Verifies that a new comment was submitted
assert len(comments_after) == len(comments_before) + 1, "Problem with counting comments"

sleep(1)
# Closing current browser
browser.close()
