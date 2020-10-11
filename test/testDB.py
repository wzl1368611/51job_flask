import sqlite3

dict1 = [{'link': 'https://jobs.51job.com/wuxi/123272867.html?s=01&t=0', 'position': '金风慧能-高级Python开发工程师(J15452)',
          'company': '金风科技-风机单元-金风慧能', 'com_href': 'https://jobs.51job.com/all/co3900593.html', 'area': '无锡',
          'exp': '5-7年经验', 'edu': '本科', 'num': '招1人', 'date': '06-30发布', 'salary': '1.5-2.5万/月',
          'welfare': '五险一金|补充医疗保险|绩效奖金|定期体检|餐饮补贴',
          'task': '工作职责:1、完成程序设计、开发、单元测试、消缺等工作；2、按照公司质量管理体系要求,参与软件工程文档编写,'
                  '发布和维护。任职资格:1、3年及以上Python开发经验；2、熟练使用下面技术中的一种或几种：a)	熟练使用MongoDB/PostgreSQL数据库；b)	'
                  '熟练使用一种Python下的REST或gRPC开发框架；c)	'
                  '熟练使用Kafka；3、熟练使用Linux操作系统；4、熟悉分布式系统设计，有高并发开发经验；5、年满18周岁。职能类别：Python开发工程师 ',
          'contact': ''}]
path = 'job.db'


def init_db(dbpath):
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


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    stt = ''
    stt_key = ''
    for data in datalist:
        for key, value in data.items():
            value = '"' + value + '"'
            stt = stt + value + ','
            stt_key = stt_key + key + ','

        # sql = 'insert into job_info(link,position,company,com_href,area,exp,edu,num,date,salary,welfare,task,contact) values (%s)' % (
        # stt[:-1])
        sql = 'insert into job_info(%s) values (%s)' % (stt_key[:-1], stt[:-1])
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
    cursor.close()
    conn.close()

    print("ok")


if __name__ == '__main__':
    # init_db(path)
    saveData2DB(dict1, path)
