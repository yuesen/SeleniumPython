from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://p.le1bao.com/Home/Login')
driver.implicitly_wait(30)
def login():
    driver.find_element_by_id('loginAccount').send_keys('15201688501')
    driver.find_element_by_id('loginPassword').send_keys('123456')
    driver.find_element_by_id('btnSubmit').click()
login()
sleep(5)
json_cookie = driver.get_cookies()
dict_cookie = json_cookie[0]

driver.quit()
sleep(5)

driver = webdriver.Chrome()
driver.get('http://p.le1bao.com/Home/Login')

driver.add_cookie(dict_cookie)
sleep(5)
driver.refresh()





