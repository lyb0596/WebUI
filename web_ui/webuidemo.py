#调用安装selenium
from selenium import webdriver
from time import sleep

#去掉黄条
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('headless')

#生成一个ChromeDriver
driver = webdriver.Chrome()

#访问指定的路径
driver.get("https://www.baidu.com")
print(driver.title)

driver.find_element_by_id('kw').send_keys('test')
driver.find_element_by_id('su').click()

#等待
sleep(2)
driver.quit()

#点击第一条连接
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()