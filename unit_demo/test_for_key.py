import unittest
from time import sleep
from web_ui.test_keywords_demo import TestKeyWords
from ddt import ddt, data, unpack
import time

@ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self):
        self.tk = TestKeyWords('http://www.baidu.com', 'chrome')
        #self.tk.implicitly_wait(0.2) # 等待0.2秒
        print('setUp')

    # 后置条件
    def tearDown(self):
        self.tk.quit_browser()
        print('tearDown')

    # 测试用例1
    # *表示基于元组的形式进行处理，**表示字典
    # @data(['id','虚竹'],['id','ABC'])
    # @unpack
    @data('123','ABC')
    def test_1(self,input_value1):
        self.tk.input_text('id', 'kw', input_value1)
        self.tk.clicek_element('id', 'su')
        sleep(3)

    # 测试用例2
    # def test_2(self):
    #     self.tk.input_text('id', 'kw', 'abc')
    #     self.tk.clicek_element('id', 'su')
    #     sleep(1)


if __name__ == '__main__':
    unittest.main()
