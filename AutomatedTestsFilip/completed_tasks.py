from selenium import webdriver
from time import sleep

# the purpose of this automated test case is to show on the screen the completed tasks


xp_expr_completed_tasks = '//*[@id="paginator"]/a'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://demo.fluxday.io/users/sign_in')
browser.find_element_by_xpath('//*[@id="user_email"]').send_keys('emp1@fluxday.io')
browser.find_element_by_xpath('//*[@id="user_password"]').send_keys('password')
browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/button').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[2]/a').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="pane2"]/div[1]/dl/dd[2]/a').click()
sleep(1)

completed_tasks = browser.find_elements_by_xpath(xp_expr_completed_tasks)
assert len(completed_tasks) != 0, "There are no completed tasks"
assert len(completed_tasks) > 0, "Problem with completed tasks"
sleep(2)
browser.close()
