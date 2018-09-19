from selenium import webdriver
import time

dr = webdriver.Chrome()
#直接登录微小说大赛的网页
dr.get("http://data.weibo.com/hittop/home?actid=281")

# 进入微博主页面竟然不能用，尴尬：dr.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[5]/div/a[1]').click()
#等待60秒扫码进入微博账号
time.sleep(60)

#找到‘查看更多’ ：
#1. 可行，用x_path方法：//*[@id="pl_hittop_rank"]/div[3]/p/a
#2. 实现不了，用link_text方法：dr.find_element_by_link_text('查看更多').click()
dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
time.sleep(10)
print('点击查看更多')
#等加载10秒

dr.find_element_by_xpath('//*[@id="pl_hittop_rank"]/div[3]/p/a').click()
time.sleep(10)

'''
#dr.implicitly_wait(10)
#要用其他包，如汤，selenium不可能这样实现：第一个方法：点右键复制xpath，然后再修改一下xpath，就可以点击到投票了，这是个很笨的方法
#dr.find_element_by_link_text("不是一见不钟情").click()           //*[@id="pl_hittop_rank"]/div[3]/dl/dd[22]/span[3]/a
'''

#投30次
for x in range(30):
    n = 22
    while n > 0:
        #获取名称
        xpath_n = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/span[3]/a'
        data = dr.find_element_by_xpath(xpath_n).text
        if data == "不是一见不钟情":
            xpath_tkt = '//*[@id="pl_hittop_rank"]/div[3]/dl/dd[' + str(n) + ']/p/a'
            #第二个笨方法：短时间内排名不变，直接用xpath定位投票的地方//*[@id="pl_hittop_rank"]/div[3]/dl/dd[22]/p/a
            dr.find_element_by_xpath(xpath_tkt).click()
            print('目标为第' + str(n+3) + '名')
            time.sleep(10)
            break
        n = n - 1

    #点击分享的xpath位置： /html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]
    dr.find_element_by_xpath("/html/body/div[6]/div/table/tbody/tr/td/div/div[2]/div/p/a[1]").click()
    print('分享成功第' + str(x+1) + '次')
    time.sleep(200)

print('投票30次完毕，退出')
dr.quit()
