# coding = utf-8
from time import sleep,ctime
from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()
# 驱动文件路径
driverfile_path = "C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
# 启动浏览器
options.binary_location = "C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
def setup_module():
    print("测试文件执行开始：start")
def teardown_module():
    print("测试文件执行结束：end")
class TestSelenium():
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(driverfile_path,chrome_options=options)
    def teardown_class(self):
        # 退出
        driver.quit()
    def test_1(self):
        print("第一个测试用例")
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
        # 通过id定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('Test selenium')
        driver.find_element_by_id('su').click()
        sleep(3)
    def test_2(self):
        print("第二个测试用例")
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
        # 通过id定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('')
        driver.find_element_by_id('su').click()
        sleep(3)
    def test_3(self):
        print("第三个测试用例")
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
        # 通过id定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('中文')
        driver.find_element_by_id('su').click()
        sleep(3)
    def test_4(self):
        print("第四个测试用例")
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
        # 通过id定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('drop database admin')
        driver.find_element_by_id('su').click()
        sleep(3)
    def test_5(self):
        print("第五个测试用例")
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
        # 通过id定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('@#$%^&*')
        driver.find_element_by_id('su').click()
        sleep(3)