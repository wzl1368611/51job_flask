import re

import requests
import time
from bs4 import BeautifulSoup
from urllib import request, parse
import urllib
import sqlite3

jobData = {}
jobList = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363 "
}


def main():
    all_url = get_urlList()  # 获取所有url地址
    detail = getData(all_url)  # 获取所有数据
    savedb = 'job2.db'  # 数据库的名称
    saveData(detail, savedb)


def askUrl(url):
    # print('url')
    html = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
    # print(html)

    return html


# "job_href":"https:\/\/51rz.51job.com\/job.html?jobid=115980776","job_name"


def get_urlList():
    """
    获取具体的url地址
    :return: url列表
    """
    # print('urlList')
    urlList = []
    keyword = input("请输入查询的职位：")
    kw = urllib.parse.quote(keyword)
    new_kw = urllib.parse.quote(kw)
    for page in range(1, 21):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99," + kw + ",2," + str(page) + ".html"
        print(url)
        html = askUrl(url)
        '''
        soup = BeautifulSoup(html, 'html.parser')
        # data = soup.select(".el .t1 span a")
        data = soup.select("div .j_joblist .e .el")
        '''
        data = []
        a = '"job_href":"(.*?)","job_name"'  # 用正则表达式解析html
        pattern = re.compile(a)
        data = pattern.findall(html)
        # print(data, '---------------------')
        if len(data) == 0:
            break
        for item in data:
            # href = item['href']
            # print(href)

            href = item.replace('\\', '')

            # print(href)
            # href = href.split('/', 1)[0]+'//'+href.split('/', 1)[1]
            # print(href)
            urlList.append(href)
        print(urlList)
    return urlList


def getData(url_lists):  # 获取数据并保存，将所有数据存储到joblist列表中
    """
    拿到单个的url,爬取页面的内容，解析并清洗提取数据
    :param url_lists:
    :return: joblist    所有的内容列表
    """
    for index in range(len(url_lists)):

        link = url_lists[index]
        html = askUrl(link)
        # print(html)

        soup = BeautifulSoup(html, "html.parser")

        data = soup.select(".tHeader.tHjob .in .cn h1")
        if len(data) == 0:
            position = ''
        else:
            position = data[0]['title']

        data1 = soup.select(".tHeader.tHjob .in .cn .cname .catn")
        if len(data1) == 0:
            company = ''
            com_href = ''
        else:
            company = data1[0]['title']
            com_href = data1[0]['href']
        # print(company, com_href, "===========")

        data2 = soup.select(".tHeader.tHjob .in .cn .msg.ltype")
        if len(data2) == 0:
            area = ''
            exp = ''
            edu = ''
            num = ''
            date = ''
        else:
            series = data2[0]['title']
            specific = series.split('|')
            # print(len(specific), '---------------------列表数量')
            num = ''
            date = ''
            if len(specific) == 3:
                area = specific[0].strip()
                exp = specific[1].strip()
                edu = specific[2].strip()
            elif len(specific) == 4:
                area = specific[0].strip()
                exp = specific[1].strip()
                edu = specific[2].strip()
                num = specific[3].strip()
            elif len(specific) == 5:
                area = specific[0].strip()
                exp = specific[1].strip()
                edu = specific[2].strip()
                num = specific[3].strip()
                date = specific[4].strip()
            # date = specific[4].strip()
            # print(area, exp, edu, num, date)
        # print(area, exp, edu, num, date)
        date3 = soup.select(".tHeader.tHjob .in .cn .jtag .t1 .sp4")
        content = ""
        welfare = ''
        if len(date3) == 0:
            welfare = ''
        else:
            # print(len(date3), type(date3), "========")

            for i in range(len(date3)):
                content = content + date3[i].text + "|"
                # print(date3[i].text)
            list_str = list(content)
            list_str.pop(-1)
            list_str = ''.join(list_str)
            welfare = list_str
        # print(welfare, "===============")

        data4 = soup.select(".tHeader.tHjob .in .cn strong")
        if len(data4) == 0:
            salary = ''
        else:
            salary = data4[0].text
        # print(salary)

        contact = ''
        data5 = soup.select(".tCompany_main .tBorderTop_box .bmsg.inbox .fp .label")
        pattern = re.compile('<p class="fp"><span class="label">.*?</span>(.*?)</p>')
        info = pattern.findall(html)
        try:
            if len(data5) == 0 or len(info) == 0:
                contact = ''
            else:
                contact = contact + data5[2].text + info[len(info) - 1]
        except Exception as e:
            contact = ''

        # print(contact, "------------------")
        # break
        task = ''
        data6 = soup.select(".tCompany_main .tBorderTop_box .bmsg.job_msg.inbox p")
        if len(data6) == 0:
            task = ''
        else:
            for j in data6:
                task = task + j.text
            task.replace('\t', '')
            task.strip()
            task.replace(' ', '')
            # print(task, '=======================task')
        # break
        # print(task, "-----------------------")

        jobData1 = {'link': link, 'position': position, 'company': company, 'com_href': com_href,
                    'area': area, 'exp': exp, 'edu': edu, 'num': num, 'date': date, 'salary': salary,
                    'welfare': welfare, 'task': task, 'contact': contact}
        jobList.append(jobData1)
        # print('第' + str(index + 1) + '条数据', jobData1)
    return jobList


'''
@lens为存储数据的列表
@path为数据库的名称
'''


def saveData(lens, path):  # 存储数据到数据库中，可以更新数据库
    """
    :param lens: 数据列表
    :param path: 数据库路径
    :return: nothing
    """
    # print('saveData')
    saveData2DB(lens, path)


# 初始化数据库
def init_db(dbpath):
    """
    :param dbpath: 数据库路径
    :return: nothing
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = '''
        create table job_info(
        id integer not null primary key autoincrement,
        link varchar(255) ,
        position varchar(255),
        salary varchar(50),
        area varchar(25),
        exp varchar(25),
        edu varchar(25),
        num varchar(50),  
        date varchar(50),
        task text, 
        contact text,
        welfare text, 
        company varchar(50) ,
        com_href varchar(255)


        )
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def saveData2DB(datalist, dbpath):  # 具体的跟新数据库的操作
    """
    :param datalist: 数据列表
    :param dbpath: 数据库的路径
    :return: nothing
    """
    # init_db(dbpath)     # 初始化数据库
    conn = sqlite3.connect(dbpath)  # 连接数据库更新数据
    cursor = conn.cursor()

    for data in datalist:   # 从列表中取出每条的数据
        stt = ''        # sql语句中的value
        stt_key = ''        # sql语句中的key
        for key, value in data.items():     # 取出对应数据的k、v值
            value = '"' + value + '"'
            stt = stt + value + ','
            stt_key = stt_key + key + ','

        # sql = 'insert into job_info(link,position,company,com_href,area,exp,edu,num,date,salary,welfare,task,
        # contact) values (%s)' % ( stt[:-1])
        try:
            sql = 'insert into job_info(%s) values (%s)' % (stt_key[:-1], stt[:-1])
            print(sql)

            # print(sql)
            # print(sql)
            # data['link'], data['position'], data['salary'], data['area'], data['exp'], data['edu'],
            # data['date'], data['task'], data['contact'], data['welfare'], data['company'], data['com_href'])
            # sql = '''
            #         insert into job_info (info_link,pic_link,cname,ename,score,rated,introduction,info) values(%s)
            #     ''' % (",".join(data))
            # print(sql)
            cursor.execute(sql)
            conn.commit()
            # cursor.execute(sql)
            # conn.commit()
        except Exception as e:
            pass
    cursor.close()
    conn.close()

    print("ok")


if __name__ == '__main__':
    main()
    # init_db('job2.db')      # 创建新的数据库的时候使用
