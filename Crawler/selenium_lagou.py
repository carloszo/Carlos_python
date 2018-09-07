#!/usr/bin/python
#-*- coding:utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import time
import xlrd,xlwt

def crawler():
    driver=webdriver.Chrome()
    driver.get('https://passport.lagou.com/login/login.html')
    # print driver.page_source
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[1]/input")
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[1]/input").send_keys("anni@cishao.cn")
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[2]/input")
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[2]/input").send_keys("a12345")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[5]/input").click()
    time.sleep(5)
    driver.get('https://easy.lagou.com/resume/list.htm?can=false&needQueryAmount=false&parentPositionIds=')
    consume_info_list = set()
    for i in range(2,22):
        temp_list = []
        consume_xpath =  '//*[@id="resumeSearchForm"]/div[2]/div[3]/table/tbody/tr[2]/td[{}]/a'.format(i)
        driver.find_element_by_xpath(consume_xpath).click()
        time.sleep(5)
        consume_page = driver.page_source
        soup = bs(consume_page,'lxml',from_encoding="utf8")
        name = soup.find("span",{'class':'candidate-name'}).text
        tel_num = soup.find("i",{'class':'split_phone'}).text
        email = soup.find("a",{'class':'info-email-url'}).text
        temp_list = [name,tel_num,email]
        consume_info_list.add(temp_list)
        print name+" 信息抓取完毕！"
    return consume_info_list


#写入Excel
#content为二维列表
def write_excel(content,filename):
    data = xlrd.open_workbook("/Users/apple/Downloads/processed_excels/import-2.xls")
    table = data.sheets()[0]
    first_row = table.row_values(0)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    line_num = 0
    for i in range(len(first_row)):
        sheet1.write(line_num, i, first_row[i])
    line_num = 1

    for row in content:
        if line_num<len(content):
            # [name, tel_num, email, profession]
            sheet1.write(line_num, 0, row[0])       #姓名
            sheet1.write(line_num, 5, row[1])       #工作电话
            # print row[1]
            sheet1.write(line_num, 15, row[2])       # 邮箱
            # print row[2]
            # sheet1.write(line_num, 12,row[2])       #公司名
            # sheet1.write(line_num, 24, row[3])  # 职务
            # print row[3]
        line_num+=1
    print " 写入完成！"
    f.save(filename)

if __name__ =="__main__":
    consume_info_list = crawler()
    filename = "/Users/apple/Downloads/lagou_import.xls"
    write_excel(consume_info_list,filename)

# driver.find_element_by_xpath('//*[@id="resumeSearchForm"]/div[2]/div[3]/table/tbody/tr[2]/td[1]/a').click()
# driver.find_element_by_xpath('//*[@id="resumeSearchForm"]/div[2]/div[3]/table/tbody/tr[3]/td[1]/a').click()
# driver.find_element_by_xpath('//*[@id="resumeSearchForm"]/div[2]/div[3]/table/tbody/tr[21]/td[1]/a').click()


# print  driver.page_source

# driver.switch_to.frame('loginIframe')
# driver.find_element_by_id('al_u').click()
# driver.find_element_by_id('al_u').clear()
# driver.find_element_by_id('al_u').send_keys('carloszo@qq.com')
# driver.find_element_by_id('al_p').click()
# driver.find_element_by_id('al_p').clear()
# driver.find_element_by_id("al_p").send_keys('a12345')
# time.sleep(5)
# driver.find_element_by_id("al_submit").click()
# print driver.page_source
# driver.find_element_by_css_selector('site_new').click()
# print driver.page_source
# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element_by_id('login-email').click()
# driver.find_element_by_id('login-email').clear()
# driver.find_element_by_id('login-email').send_keys('carlos@lieneng.com.cn')
# driver.find_element_by_id('login-password').click()
# driver.find_element_by_id('login-password').clear()
# driver.find_element_by_id('login-password').send_keys('Anniivan0202')
# driver.find_element_by_id('login-submit').click()
# driver.get('http://www.linkedin.com/in/michael-xu-6930991/')
# print driver.page_source
# driver.switch_to.frame('contentFrame')
# html = driver.page_source
#driver.find_element_by_xpath("//span[@class='txt']")
#print driver.page_source
#browser.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
#browser.find_element_by_link_text("About").click()
#driver.get("http://music.163.com/#/discover/toplist")
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[2]/span/a/em").click()
# driver.find_element_by_xpath("//div[@id='g-topbar']/div/div/ul/li[3]/span/a/em").click()
# driver.find_element_by_css_selector("in_txt").click()
# html=driver.page_source
# print html
# driver.close()
# driver.quit()
# soup = bs(html,'lxml')
# urls =  soup.findAll('a',href=re.compile(r'song\?id=(\d+)'))
# songid=set()
# for url in urls:
#     songid.add(url['href'].split('?')[-1])


