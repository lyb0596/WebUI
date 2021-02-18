import unittest
from time import sleep
from web_ui.test_keywords_demo import TestKeyWords


class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self):
        self.tk = TestKeyWords('http://www.baidu.com', 'chrome')

        print('setUp')

    # 后置条件

    def tearDown(self):
        self.tk.quit_browser()
        print('tearDown')

    # 测试用例1
    def test_1(self):
        self.tk.input_text('id', 'kw', '虚竹')
        self.tk.clicek_element('id', 'su')
        sleep(3)

    # 测试用例2
    def test_2(self):
        self.tk.input_text('id', 'kw', 'abc')
        self.tk.clicek_element('id', 'su')
        sleep(3)

if __name__ == '__main__':
    unittest.main()
