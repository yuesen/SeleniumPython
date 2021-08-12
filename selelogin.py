import sys
sys.path.append(r"D:\Python37\Lib\site-packages")    # 不需要在往后变加上selenium包了，加上就报错

from selenium import webdriver
import time

def login(username,password):
    driver = webdriver.Chrome()
    driver.get('http://p.le1bao.com/Home/Login')
    driver.find_element_by_id('loginAccount').send_keys(username)
    driver.find_element_by_id('loginPassword').send_keys(password)
    driver.find_element_by_id('btnSubmit').click()
    time.sleep(3)
    if "乐意保测试商户" in driver.page_source:
        print("登录成功")
    else:
        print("登录失败")
    driver.quit()
login(15201688501,123456)



