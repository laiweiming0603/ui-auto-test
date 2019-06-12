
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.60.146:8080/demo1.html')
action_chains = ActionChains(driver)


def link_qiehuan():
    link_el = driver.find_element_by_partial_link_text('京东')
    action_chains.key_down(Keys.CONTROL).click(link_el).key_up(Keys.CONTROL).perform()
    window_handles = driver.window_handles
    for i in window_handles:
        driver.switch_to.window(i)
        if driver.title.__contains__('京东'):
            break
    time.sleep(5)

if __name__ == '__main__':
    link_qiehuan()
    driver.quit()