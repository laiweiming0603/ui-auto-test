from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.60.146:8080/demo1.html')

def input_demo():
    time.sleep(5)
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    time.sleep(5)
    input_el.send_keys('且随疾风前行')
    time.sleep(5)
    input_el.clear()
    input_el.send_keys('死亡如风，常伴吾身')
    time.sleep(5)

def input_demo2():
    # 通过id定位
    feil_el = driver.find_element_by_id('file1')
    feil_el.send_keys('C:/Users/Administrator/Desktop/搜狗截图20190530101858.png')
    time.sleep(5)
    # 通过name定位
    radio_el = driver.find_elements_by_name('radio')
    radio_el[0].click()
    time.sleep(2)
    radio_el[1].click()
    time.sleep(5)

def checkbox_demo3(driver):
    checkbox_els = driver.find_elements_by_class_name('checkbox')
    for i in range(len(checkbox_els)):
        checkbox_els[i].click()
    # checkbox_els[0].click()
    # checkbox_els[1].click()
    # checkbox_els[2].click()

def input_demo4():
    button_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td[2]/input')
    button_el.click()
    time.sleep(2)
    # 确认弹框
    driver.switch_to.alert.accept()
    # 取消弹框
    # driver.switch_to.alert.dismiss()

def input_demo5():
    password_el = driver.find_element_by_xpath('//input[@type="password"]')
    password_el.send_keys('aabbcc')
    time.sleep(2)

def input_demo6():
    password_el = driver.find_element_by_xpath('//input[@type="number"]')
    password_el.send_keys('10')
    time.sleep(2)

def xialakuag_demo():
    select_el = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    s = Select(select_el)
    # 通过索引选择
    s.select_by_index(1)
    time.sleep(2)
    # 通过value选择
    s.select_by_value('z1')
    time.sleep(2)
    # 通过展示文本选择
    s.select_by_visible_text('周龙3')
    time.sleep(2)


def chaolianjiedemo():
    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element_by_partial_link_text('度娘').click()
    driver.back()
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    # 窗口最大化
    driver.maximize_window()
    # 最小化
    driver.minimize_window()
def tijiao_demo():
    time.sleep(1)
    driver.find_elements_by_xpath('//input[@type="submit"]').clear()


if __name__ == '__main__':

    # input_demo()
    # input_demo2()
    # checkbox_demo3()
    # input_demo4()
    # input_demo5()
    # input_demo6()
    # xialakuag_demo()
    chaolianjiedemo()
    # tijiao_demo()


    time.sleep(2)

    # 关闭浏览器
    driver.quit()
    # driver.close() 也可关闭，但不关闭驱动程序