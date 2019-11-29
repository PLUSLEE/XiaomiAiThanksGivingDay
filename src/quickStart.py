# -*- coding: utf-8 -*-
'''
获取小米感恩节中小爱同学的所有祝福卡片
'''
from selenium import webdriver
from grab import Grab
import os
import requests
import time


def getSources(i=None):
    level = driver.find_element_by_class_name('index_title__2AG9z').get_attribute('textContent')
    # print(level)
    # TODO 若发现此时src==上一步src，则判定结束，退出浏览器。并发出通知已经完成数据下载；或程序异常，发送错误代码到手机
    pic_url = driver.find_element_by_class_name('index_letterImg__3DlbL').get_attribute('src')
    # print(pic_url)

    # 获取图片
    img = requests.get(pic_url)

    # 保存图片到指定文件夹下
    path = 'D:\Sources\XiaoMiThanksgivingDay\pic'
    # 如果没有对应文件夹，自动创建文件夹
    if not os.path.isdir(path):
        os.mkdir(path)
    paths = path + '\\'

    # 按照level和读取顺序保存图片
    file = open(paths + level + str(i) + '.jpg', 'ab')
    file.write(img.content)
    print(level + str(i), '文件保存成功！')
    file.close()

    return pic_url


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://i.ai.mi.com/h5/ai-thanksgiving-letter-fe/#/letter')

    for i in range(1, 300):
        old_url=getSources(i)


        # 点击进入下一张图片
        driver.find_element_by_class_name('index_nextButton__2CRzD').click()
        time.sleep(5)
