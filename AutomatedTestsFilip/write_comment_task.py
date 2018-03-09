from selenium import webdriver
from time import sleep

# the purpose of this automated test case is to verify it is possible to write a comment for a task

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
browser.find_element_by_xpath('//*[@id="paginator"]/a[1]/div').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="pane3"]/div[2]/div/div[2]/a').click()
sleep(1)

comments_before = browser.find_elements_by_xpath('//*[@id="pane3"]/div[2]/div/div[2]/div')
browser.find_element_by_xpath('//*[@id="comment_body"]').send_keys('Test comment 1')
browser.find_element_by_xpath('//*[@id="comment_body"]').submit()
sleep(1)
comments_after = browser.find_elements_by_xpath('//*[@id="pane3"]/div[2]/div/div[2]/div')
sleep(1)
# print(len(comments_before))
# print(len(comments_after))
assert len(comments_after) == len(comments_before) + 1, "Problem with counting comments"
sleep(2)
browser.close()
