from flask import Flask, render_template
import sqlite3
import os
import logging

# from time import *
logging.basicConfig(
    filename=os.path.join(os.getcwd(), 'all.log'),
    level=logging.WARNING,
    format='%(asctime)s %(filename)s : %(levelname)s %(message)s',
    filemode='a',
    datefmt='%Y-%m-%d %A %H:%M:%S',
)
logging.info('this is a message')
app = Flask(__name__)


@app.route('/')
def index():
    jobList = []
    conn = sqlite3.connect("job2.db")
    cursor = conn.cursor()
    sql = "select  * from job_info order by id asc "
    data = cursor.execute(sql)
    for item in data:
        jobList.append(item)
        # logging.info(item['position'] + '-' + item['salary'] + '-' + item['area'] + '-' + item['exp'] + '-' + item[
        #     'date'] + '-' + item['company'])
        # print(jobList, '==================')
        # logging.info(type(item))
        # logging.info(item[2:9], item[12])
        logging.info((item[0], item[2:9], item[12]))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('index.html', jobList=jobList)


def process_data(sql):  # 与数据库连接处理数据
    jobList = []
    conn = sqlite3.connect("job2.db")
    cursor = conn.cursor()

    data = cursor.execute(sql)
    for item in data:
        jobList.append(item)
    # print(jobList, '==================')
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/cards')
def cards():
    return render_template('cards.html')


@app.route('/charts')
def charts():
    # 0-6 6-8  8-12 12-15 15-20 20-30 30-40 40
    #  工资均值所在的区间 把千为单位的转成万
    #  cityName 上海 长沙 杭州 苏州 深圳 广州 北京 西安 东莞 南京 昆明 济南
    list2 = []
    for j in range(2):
        if j == 0:
            conn = sqlite3.connect("job2.db")
            cursor = conn.cursor()
            sql = "select  salary from job_info  "
            data = cursor.execute(sql)
            #   处理数据

            count0 = 0
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            count7 = 0
            for i in data:
                # print(i, type(i))
                avg = 0
                i = str(i)
                #  str(x).split('/')[0].replace("('", "")
                list01 = i.split('/')[0].replace("('", "")
                num = list01.split('-')
                try:
                    if list01.find('千') != -1:
                        # print(num[1][:-1], '---------------===========')
                        avg = (float(num[0]) + float(num[1][:-1])) / 20.0
                    else:
                        # print(num[1][:-1], '------------------')
                        avg = (float(num[0]) + float(num[1][:-1])) / 2.0
                    if avg < 0.6:
                        count0 += 1
                    elif 0.6 < avg < 0.8:
                        count1 += 1
                    elif 0.8 < avg < 1.2:
                        count2 += 1
                    elif 1.2 < avg < 1.5:
                        count3 += 1
                    elif 1.5 < avg < 2:
                        count4 += 1
                    elif 2 < avg < 3:
                        count5 += 1
                    elif 3 < avg < 4:
                        count6 += 1
                    elif avg > 4:
                        count7 += 1
                except Exception as e:
                    pass
            sum1 = [count0, count1, count2, count3, count4, count5, count6, count7]
            sum2 = count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7
            logging.warning(('统计工资区间总人数', sum2))
            # print(sum, "-------------")

        if j == 1:
            list1 = []
            conn = sqlite3.connect("job2.db")
            cursor = conn.cursor()
            sql = "select  area from job_info order by id asc "
            data1 = cursor.execute(sql)
            for dd in data1:

                dd = str(dd)
                # print(dd, "---------")
                if dd.find('-') != -1:
                    city = dd.split('-')[0].replace("('", "")
                    # 遍历之后开始计数
                    list1.append(city)
                else:
                    list1.append(dd.replace("('", "").replace("',)", ""))
            dict1 = {'上海': list1.count('上海'), '长沙': list1.count('长沙'), '杭州': list1.count('杭州'), '苏州': list1.count('苏州'),
                     '深圳': list1.count('深圳'), '广州': list1.count('广州'), '北京': list1.count('北京'), '西安': list1.count('西安'),
                     '东莞': list1.count('东莞'), '南京': list1.count('南京'), '昆明': list1.count('昆明'), '济南': list1.count('济南')}
            dict2 = list1.count('上海') + list1.count('长沙') + list1.count('杭州') + list1.count('苏州') + list1.count('深圳') + \
                    list1.count('广州') + list1.count('北京') + list1.count('西安') + list1.count('东莞') + list1.count('南京') + \
                    list1.count('昆明') + list1.count('济南')
            logging.warning(('统计城市招聘总人数', dict2))
            print(dict1, "=========================")
            conn.commit()
            cursor.close()
            conn.close()

    # print(sum, dict1)
    return render_template('charts.html', sum1=sum1, sum2=sum2, dict1=dict1, dict2=dict2)


@app.route('/tables')
def tables():
    # jobData = {}
    jobList = []
    conn = sqlite3.connect("job2.db")
    cursor = conn.cursor()
    sql = "select  * from job_info order by id asc "
    data = cursor.execute(sql)
    for item in data:
        jobList.append(item)
        # logging.info(item)
        # logging.info(item['position'] + '-' + item['salary'] + '-' + item['area'] + '-' + item['exp'] + '-' + item[
        #     'date'] + '-' + item['company'])
        logging.info((item[0], item[2:9], item[12]))
    # print(jobList, '==================')

    conn.commit()
    cursor.close()
    conn.close()

    return render_template('tables.html', jobList=jobList)


@app.route('/buttons')
def buttons():
    return render_template('buttons.html')


@app.route('/blank')
def blank():
    return render_template('blank.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot_pwd')
def forgot_password():
    return render_template('forgot-password.html')


if __name__ == '__main__':
    app.run()
