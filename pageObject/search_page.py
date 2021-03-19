from basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    #搜索框
    input_id = (By.ID,'kw')
    #百度一下按钮
    click_id = (By.ID,'su')

    #对搜索框进行内容的输入
    def input_text(self,input_text):
        self.locator(self.input_id).send_keys(input_text)

    #点击查询那妞，实现本次搜索
    def click_element(self):
        self.locator(self.click_id).click()

    def check(self,url,input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    #调试
    sp.check(url,'abc')