# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#修改参数投票次数(s)和大概的时间间隔(s)
times = 60
interval = 70

#进入谷歌浏览器
dr = webdriver.Chrome()

#记录上一次的票数
votes = 0
votes_last = 0
pre_interval = interval - 15

#投票 times 次之后或者不能再投票时，自己退出关闭浏览器
for x in range(times):
    #刷新页面,等待60秒加载页面（第一次投票需要手动扫码登录账号，之后的投票就不用登录了）
    dr.get("http://data.weibo.com/hittop/home?actid=281")
    time.sleep(pre_interval)

    #将滚动条移动到页面的顶部
    js="var q = document.documentElement.scrollTop=0"
    dr.execute_script(js)
    time.sleep(3)

    #用x_path方法：//*[@id="pl_hittop_rank"]/div[3]/p/a
    dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
    time.sleep(5)
    dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
    time.sleep(5)

    #定义当前票数(为上一次投票时的票数)
    votes_now = votes

    #现在判断排名是不是想要的小说名，如果是就点击相应的投票按钮
    ranking = 22
    n = ranking
    while n > 0:
        #获取名称
        xpath_n = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/span[3]/a'
        data = dr.find_element_by_xpath(xpath_n).text
        #如果为目标名称，就获取当前的投票按钮位置，自己的票数和上一名的票数
        if data == "不是一见不钟情":
            ranking = n
            xpath_tkt = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(ranking) + ']/p/a'
            xpath_num = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(ranking) + ']/span[5]/i'
            xpath_last = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(ranking-1) + ']/span[5]/i'
            votes_now = int(dr.find_element_by_xpath(xpath_num).text)
            votes_last = int(dr.find_element_by_xpath(xpath_last).text)
            n = 0
            break
        n -= 1

    #如果没被限制投票，就点击投票按钮，然后分享
    if votes_now > votes :
        votes = votes_now
        dr.find_element_by_xpath(xpath_tkt).click()
        time.sleep(5)
        print('排名(๑´•ω•)：' + str(ranking+3) + '  票数(〝▼皿▼)：' + str(votes) + '  上一名票数(#ﾟДﾟ)：' + str(votes_last))
        #点击分享的xpath位置： /html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]
        dr.find_element_by_xpath("/html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]").click()
        print('分享成功' + str(x+1) + '次')
    else:
        votes = votes_now
        print('排名(๑´•ω•)：' + str(ranking+3) + '  票数(〝▼皿▼)：' + str(votes) + '  上一名票数(#ﾟДﾟ)：' + str(votes_last) + '\n请稍后再试 _(:з」∠)_ ')
        dr.quit()
        break


print('投票完毕，退出')
dr.quit()

'''
待完善
1.自动登录微博，自动获取cookie
2.添加投票时间
3.判断当前页面目标是否存在，如果没有再找“查看更多” while dr.find_elements_by_link_text("不是一见不钟情") == False:
4.判断是否限制投票的部分还有一定的问题
......
'''