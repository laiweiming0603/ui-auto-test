from selenium import webdriver
import time
driver=webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.60.146:8080/demo1.html')

def input_demo():
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    time.sleep(2)
    input_el.send_keys('双眼失明丝毫不影响我追捕敌人')
    time.sleep(2)
    input_el.clear()
    time.sleep(2)

def wenbenshangchuan():
    file_el = driver.find_element_by_id('file1')
    time.sleep(2)
    file_el.send_keys('C:/Users/Administrator/Desktop/搜狗截图20190530101858.png')
    time.sleep(2)

def danxuan():
    radio_els = driver.find_elements_by_name('radio')
    time.sleep(2)
    radio_els[0].click()
    time.sleep(2)
    radio_els[1].click()
    time.sleep(2)

def duoxuan():
    checkbox_els = driver.find_elements_by_class_name('checkbox')
    checkbox_els[1].click()
    time.sleep(2)

def anniu():
    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    time.sleep(2)
    button_el.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)

def mima():
    password_el = driver.find_element_by_xpath('//input[@type="password"]')
    time.sleep(2)
    password_el.send_keys('lalala')
    time.sleep(2)
    password_el.clear()
    time.sleep(2)

def num():
    num_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[8]/td[2]/input')
    time.sleep(2)
    num_el.send_keys(123)
    time.sleep(2)
    num_el.clear()
    time.sleep(2)



if __name__ == '__main__':
    input_demo()
    wenbenshangchuan()
    danxuan()
    duoxuan()
    anniu()
    mima()
    num()