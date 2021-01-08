from PIL import Image
from numpy.random.tests.test_generator_mt19937 import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import re
import time
import argparse
import yaml
import successFlag
import identifyVerificationCode


class ClockIn():
    verificationCode = ''

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=seleniumFirefoxDriver_path)
        self.dayTemp = 36.2
        self.nightTemp = 36.3
        # window eleniumFirefoxDriver路径
        # self.driver = webdriver.Firefox(executable_path="D:/seleniumFirefoxDriver/geckodriver")

    def setup_method(self):
        # self.vars = {}
        self.driver.get("https://fangkong.hnu.edu.cn/app/")
        self.driver.set_window_size(500, 800)

    def teardown_method(self):
        self.driver.quit()

    def randomTemp(self):

        while (True):
            ran1 = random.random()
            ran2 = random.random()
            self.dayTemp += ran1
            self.dayTemp += ran2
            if self.dayTemp != self.nightTemp and self.dayTemp < 37.2 and self.nightTemp < 37.2:
                break
            else:
                self.dayTemp = 36.1
                self.nightTemp = 36.2

        self.dayTemp = str(self.dayTemp)[0:4]
        self.nightTemp = str(self.nightTemp)[0:4]
        print('昨夜体温：', self.nightTemp)
        print('今早体温：', self.dayTemp)

        return self.dayTemp, self.nightTemp

    def login(self):

        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input:nth-child(2)").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input:nth-child(2)").send_keys(username)

        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").send_keys(password)

        self.driver.find_element_by_xpath("//input[@type='number']").click()
        self.driver.find_element_by_xpath("//input[@type='number']").send_keys(self.verificationCode)

        self.driver.find_element(By.CSS_SELECTOR, ".loginBtn").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".loginBtn")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()

    # 双峰带单选框
    def clock_in_SF(self):
        # 定位框
        self.driver.find_element(By.CSS_SELECTOR, ".van-cell__value > span").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'河北省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'内蒙古自治区\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'吉林省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'上海市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'浙江省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'福建省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'山东省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'湖北省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'湖南省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'湘潭市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'邵阳市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'常德市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'益阳市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'永州市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'娄底市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'双峰县\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".van-picker__confirm").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").send_keys(home)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(3) .van-radio:nth-child(2) .van-icon")
        self.driver.execute_script('arguments[0].click()', element)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(4) .van-radio:nth-child(1) > .van-radio__label")
        self.driver.execute_script('arguments[0].click()', element)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(5) .van-radio:nth-child(2) > .van-radio__label")
        self.driver.execute_script('arguments[0].click()', element)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(6) .van-radio:nth-child(2) > .van-radio__label")
        self.driver.execute_script('arguments[0].click()', element)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(7) .van-radio:nth-child(2) > .van-radio__label")
        self.driver.execute_script('arguments[0].click()', element)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".template-content-list:nth-child(8) .van-radio:nth-child(2) > .van-radio__label")
        self.driver.execute_script('arguments[0].click()', element)

        self.driver.find_element(By.CSS_SELECTOR, ".btnDaka").click()


    # 只有体温
    def clock_in_second(self):
        dayTemp = 36.2
        nightTemp = 36.3
        while (True):
            ran1 = random.random()
            ran2 = random.random()
            dayTemp += ran1
            dayTemp += ran2
            if dayTemp != nightTemp and dayTemp < 37.2 and nightTemp < 37.2:
                break
            else:
                dayTemp = 36.1
                nightTemp = 36.2

        dayTemp = str(dayTemp)[0:4]
        nightTemp = str(nightTemp)[0:4]
        print('昨夜体温：', nightTemp)
        print('今早体温：', dayTemp)

        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(2) > div > input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(2) > div > input").send_keys(self.nightTemp)
        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(3) > div > input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(3) > div > input").send_keys(self.dayTemp)
        self.driver.find_element(By.CSS_SELECTOR, ".m-kong:nth-child(3)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .van-notice-bar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".travel-box:nth-child(4) .travel-card-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".travel-box:nth-child(6) em").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .btnDaka").click()
        # ele = self.driver.find_element(By.CSS_SELECTOR, ".btnDaka:nth-child(8)")
        # ele.click()
        # if ele.is_displayed():
        #     ele.click()

    # 长沙带体温
    def clock_in_CS(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".van-picker-column:nth-child(1)").click()
        self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div").click()
        self.driver.find_element(By.XPATH,
                                 "//div[2]/div[2]/div[2]/div").click()

        self.driver.find_element(By.XPATH, "//li[contains(.,\'河北省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'内蒙古自治区\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'吉林省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'上海市\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'浙江省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'福建省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'山东省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'湖北省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'湖南省\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'天心区\')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(.,\'岳麓区\')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'确认\')]").click()

        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(2) > .template-content-list .van-field__control").send_keys("湖南大学")

        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(2) > div > input").send_keys(self.nightTemp)
        self.driver.find_element(By.CSS_SELECTOR, ".travel-nav:nth-child(3) > div > input").send_keys(self.dayTemp)
        # self.driver.find_element(By.CSS_SELECTOR, ".travel-box:nth-child(5) .travel-card-title").click()
        # 滑动条下拉到底部
        js = "window.scrollTo(0,100000)"
        self.driver.execute_script(js)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".btnDaka:nth-child(9)").click()

    def identify_code(self):
        """
        selenium截图，定位验证码图片
        """
        self.driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div[4]").click()
        time.sleep(2)
        self.driver.save_screenshot('fangkong_login.png')
        # codeEelement = self.driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div[3]/img")
        # print('验证码图片', codeEelement, type(codeEelement))
        # imgSize = codeEelement.size  # 获取验证码图片的大小
        # print('图片大小', imgSize, type(imgSize))
        # imgLocation = codeEelement.location  # 获取验证码元素坐标
        # print('图片位置', imgLocation, type(imgLocation))
        # rangle = (int(imgLocation['x']), int(imgLocation['y']), int(imgLocation['x'] + imgSize['width']),
        #           int(imgLocation['y'] + imgSize['height']))  # 计算验证码整体坐标
        # print(rangle)
        login = Image.open('fangkong_login.png').convert('RGB')
        text = identifyVerificationCode.noise_reduction(login, rangle)
        self.verificationCode = re.findall(r"\d*", text)[0]
        print('输出识别的验证码：', self.verificationCode)

    # 封装一个函数，用来判断元素标签是否存在
    def is_element_present(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    def is_success(self):
        if self.is_element_present('css selector', ".template-content-list:nth-child(4) .van-radio:nth-child(1)"):
            # 仍在填写界面
            return True
        else:
            return False

    def is_login(self):
        if self.is_element_present('css selector', "div:nth-child(1) > input:nth-child(2)"):
            # 仍在登陆界面
            return True
        else:
            return False


def wantTo():
    try:
        sign = ClockIn()
        sign.setup_method()
        time.sleep(2)

        while True:
            if sign.is_login():
                sign.identify_code()
                sign.login()
            else:
                print('登陆成功')
                break
            time.sleep(5)

        # 时间戳
        detail_time = time.strftime('%H:%M', time.localtime(time.time()))

        if sign.is_success():
            dt, nt = sign.randomTemp()
            sign.clock_in_CS()
            # dt, nt = sign.clock_in_second()
            msg = '今早 ' + detail_time + ' 体温:' + dt + '昨夜体温：' + nt
            print('打卡成功！')
            time.sleep(10)
            sign.teardown_method()

        else:
            print('打卡成功！')
            time.sleep(10)
            msg = detail_time + ' 今天已经打过卡啦.'
            sign.teardown_method()
        successFlag.Email(from_addr, email_password, to_addr, smtp_server, msg)
        print('邮件已提醒')
    except Exception as e:
        print('报错:', e)
        print('再试一次')
        wantTo()


# 载入参数
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='default.yml', help='configure of clockIN')
args = parser.parse_args()
config = yaml.load(open(args.config, 'r', encoding='UTF-8'), Loader=yaml.FullLoader)
seleniumFirefoxDriver_path = config['seleniumFirefoxDriver_path']
username = config['username']
password = config['web_password']
home = config['home']
rangle = config['rangle']

from_addr = config['from_addr']
email_password = config['email_password']
to_addr = config['to_addr']
smtp_server = config['smtp_server']

wantTo()
