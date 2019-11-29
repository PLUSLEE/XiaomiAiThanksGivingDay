# XiaomiAiThanksGivingDay
小米小爱同学的2019年感谢信明信片收集爬虫


2019年11月28日，把玩了好几个月的小米9SE，推送了一条消息“小爱 『同学们』的感恩信”，顺手点开开启感恩信，第一篇就是Are U OK的雷军。


![雷军亲笔明信片1.jpg](https://i.loli.net/2019/11/29/glj3ZW7MDBwkfOp.jpg)


嘿，闲来无事，顺手点点，发现小爱同学里应该都是优秀的人才啊。

出于对小米系统的喜爱，处于对小爱同学语音助手的喜爱，决定将所有的感恩信全部下载下来，留存备份。项目代号“爱了爱了”。


挑选一些自己认为比较有意思的明信片。

![工程师篇192.jpg](https://i.loli.net/2019/11/29/amnRqYzgDkhWfCJ.jpg)
![工程师篇4.jpg](https://i.loli.net/2019/11/29/RAhcovDd8amSKiV.jpg)
![产品经理篇93.jpg](https://i.loli.net/2019/11/29/ewU4pysFWkBM6Al.jpg)
![产品经理篇8.jpg](https://i.loli.net/2019/11/29/io8TdALWJb2eap9.jpg)
![产品经理篇76.jpg](https://i.loli.net/2019/11/29/38xX4hmynjptPNS.jpg)
![产品经理篇4.jpg](https://i.loli.net/2019/11/29/upRfVnh72DdZmSr.jpg)
![产品经理篇53.jpg](https://i.loli.net/2019/11/29/gYGnqmvbWPQ3F8J.jpg)
![产品经理篇26.jpg](https://i.loli.net/2019/11/29/31nXGqws9aJWLFg.jpg)
![设计师篇72.jpg](https://i.loli.net/2019/11/29/qPFHZzoc6pdk4gy.jpg)
![产品经理篇129.jpg](https://i.loli.net/2019/11/29/tTX9SJ5izaGuk3Z.jpg)


```python
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


```
----

在这些代码基础上，开始下载保存图片。因为一开始没有确认一共有多少感谢信，只设置下载到299张。后来仔细阅读发现，一共其实是608人。

所以现在这299张图片的基础上进行一个分析。图片中有部分重复，但不影响产品经理、工程师、设计师之间的比例。至于为什么会重复，答案未知。（也许代码可以修改为判断是否是同一张图片，如果是就不去下载了。然后for循环他个1000次）

  

以下是图片截图：

设计师篇：不愧是设计师，过大半比例都是涂涂画画，还挺好看。
![1.png](https://i.loli.net/2019/11/29/hXQ5CsGD63TEzYH.png)

  工程师篇：符合大家对工程师的认知，文字为主，图片为辅，不乏特色。  

![2.png](https://i.loli.net/2019/11/29/KZwgaTuOULQVtpD.png)
![Image3.png](https://i.loli.net/2019/11/29/2DJbOIrsUqSa3WH.png)
![Image4.png](https://i.loli.net/2019/11/29/sVb8cnX5CdQ1IF3.png)
![Image5.png](https://i.loli.net/2019/11/29/v8nQ1gjbcUTNBZa.png)
![Image6.png](https://i.loli.net/2019/11/29/UWXwbL4puB3NJyI.png)


产品经理篇：恩，产品经理的感谢信介于工程师与设计师之间吧，风格各异，有个性的极具个性。
![Image7.png](https://i.loli.net/2019/11/29/h3ijqxSbyBLJNo7.png)
![Image8.png](https://i.loli.net/2019/11/29/HJDmZEi9v3fUMBn.png)
![Image9.png](https://i.loli.net/2019/11/29/8WEfkZaHP7s4XwN.png)

产品经理89张，工程师179张，设计师37张。

**PM：RD：Designer=89:179:37≈3：6：1，从这个关系中可以看出小爱同学的整个项目中，开发工程师占据的大半，产品经理占据三成，设计师比例一成。**

项目源码与收集到的资源在Github上，地址：

[https://github.com/PLUSLEE/XiaomiAiThanksGivingDay](https://github.com/PLUSLEE/XiaomiAiThanksGivingDay)
