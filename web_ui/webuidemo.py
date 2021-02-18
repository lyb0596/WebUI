#调用安装selenium
from selenium import webdriver
from time import sleep

#生成一个ChromeDriver
driver = webdriver.Chrome()

#访问指定的路径
driver.get("https://www.baidu.com")

driver.find_element_by_id('kw').send_keys('test')
driver.find_element_by_id('su').click()

#等待
sleep(2)

#点击第一条连接
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()