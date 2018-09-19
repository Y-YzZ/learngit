#!/usr/bin/python
# -*- coding: utf-8 -*-
#记得加utf-8编码,这个只能放在第一行和第二行，记得待会儿保存一下

from selenium import webdriver
import time

#进入浏览器
dr = webdriver.Chrome()

# 进入微博主页面竟然不能用，尴尬，换为以下的方法：dr.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[5]/div/a[1]').click()
#直接登录微小说大赛的网页
dr.get("http://data.weibo.com/hittop/home?actid=281")
#等待60秒手动扫码进入微博账号（哭晕，还没做好）
time.sleep(60)

#找到“查看更多” ：
#1. 可行，用x_path方法：//*[@id="pl_hittop_rank"]/div[3]/p/a
#2. 实现不了，用link_text方法：dr.find_element_by_link_text('查看更多').click()
dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
time.sleep(10)
#等加载10秒
dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
time.sleep(10)

'''
#dr.implicitly_wait(10)
#要用其他包，如汤，selenium不可能这样实现：第一个方法：点右键复制xpath，然后再修改一下xpath，就可以点击到投票了，这是个很笨的方法
#dr.find_element_by_link_text("不是一见不钟情").click()           //*[@id="pl_hittop_rank"]/div[3]/dl/dd[22]/span[3]/a
#第二个笨方法：短时间内排名不变，直接用xpath定位投票的地方//*[@id="pl_hittop_rank"]/div[3]/dl/dd[22]/p/a
#最后都排除了
'''
#现在判断排名是不是想要的小说名，如果是就点击相应的投票按钮
#投票30次完成，自己退出关闭浏览器
for x in range(20):
    n = 22
    while n > 0:
        #获取名称
        xpath_n = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/span[3]/a'
        data = dr.find_element_by_xpath(xpath_n).text
        if data == "不是一见不钟情":
            xpath_tkt = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/p/a'
            dr.find_element_by_xpath(xpath_tkt).click()
            time.sleep(10)
            xpath_num = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/span[5]/i'
            votes = dr.find_element_by_xpath(xpath_num).text
            print('现在是第' + str(n+3) + '名,现有票数为' + votes + '票')
            break
        n = n - 1

    #点击分享的xpath位置： /html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]
    dr.find_element_by_xpath("/html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]").click()
    print('分享成功第' + str(x+1) + '次')
    time.sleep(60)

print('投票完毕，退出')
dr.quit()

'''
完善
1.自动登录微博，自动获取cookie
2.显示已有的票数
'''