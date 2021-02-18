from selenium import webdriver


class TestKeyWords(object):
    # 初始化
    def __init__(self, url, browser_type):
        self.driver = self.open_browser(browser_type)
        self.driver.get(url)

    # 调用浏览器
    def open_browser(self, browser_type):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
            return self.driver
        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()
            return self.driver
        else:
            print('type error')

    def locator(self, locator_type, value):
        if locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el

    # 输 入
    def input_text(self, locator_type, value, text):
        self.locator(locator_type, value).send_keys(text)

    # 点击
    def clicek_element(self, locator_type, value):
        self.locator(locator_type, value).click()

    #关闭浏览器，释放资源
    def quit_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    tk = TestKeyWords('http://www.baidu.com', 'chrome')
    tk.input_text('id', 'kw', '虚竹')
    tk.clicek_element('id', 'su')
