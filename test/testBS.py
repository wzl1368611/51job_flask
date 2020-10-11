from bs4 import BeautifulSoup
import re
# with open('job_first.html', 'r') as f:
#     html = f.read()
# # print(html)
# soup = BeautifulSoup(html, "html.parser")
# data = soup.select(".el .t1 span a")
# for item in data:
#     href = item['href']
#     print(href)

with open('html001.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

data = soup.select(".tHeader.tHjob .in .cn h1")
position = data[0]['title']

data1 = soup.select(".tHeader.tHjob .in .cn .cname .catn")
company = data1[0]['title']
com_href = data1[0]['href']
print(company, com_href, "===========")

data2 = soup.select(".tHeader.tHjob .in .cn .msg.ltype")
series = data2[0]['title']
specific = series.split('|')
area = specific[0].strip()
exp = specific[1].strip()
edu = specific[2].strip()
num = specific[3].strip()
date = specific[4].strip()
print(area, exp, edu, num, date)
date3 = soup.select(".tHeader.tHjob .in .cn .jtag .t1 .sp4")
content = ""
# print(len(date3), type(date3), "========")
for i in range(len(date3)):
    content = content + date3[i].text + "|"
    # print(date3[i].text)
list_str = list(content)
list_str.pop(-1)
list_str = ''.join(list_str)
print(list_str, "===============")

data4 = soup.select(".tHeader.tHjob .in .cn strong")
salary = data4[0].text
print(salary)

task = ''
data5 = soup.select(".tCompany_main .tBorderTop_box .bmsg.inbox .fp .label")
# print(data5[2].text, '----------------------data5')
# data7 = soup.select(".tCompany_main .tBorderTop_box .bmsg.inbox .fp")
# print(data7, '-------------------------------data7')


# <p class="fp"><span class="label">上班地址：</span>闵行区申滨南路1126号龙湖天街C栋10楼（2号/10号/17号线虹桥火车站步行8分钟）</p>
# <p class="fp"><span class="label">.*?</span>(.*?)</p>

# data8 = soup.find_all(re.compile('<p class="fp"><span class="label">.*?</span>(.*?)</p>'))
# print(data8, '--------------------------------data8')
pattern = re.compile('<p class="fp"><span class="label">.*?</span>(.*?)</p>')
info = pattern.findall(html)
task = task+data5[2].text+info[len(info)-1]
print(task, "------------------")
# print(info[len(info)-1], '---------------什么是info')


#
# pattern2 = re.compile('<p class="fp"><span class="label">(.*?)</span>.*?</p>')
# info2 = pattern2.findall(html)
# print(info2, '-----------------什么是info2')

contact = ''
data6 = soup.select(".tCompany_main .tBorderTop_box .bmsg.job_msg.inbox p")
for j in data6:
    contact = contact + j.text
print(contact, "-----------------------")
# contact = data6[0].text


# data = soup.select(".tHeader.tHjob .in .cn h1")
# data = soup.select(".tHeader.tHjob .in .cn h1")
#
#
# print(data[0])


# data = soup.select(".tHeader.tHjob .in .cn h1")
# print(data[0]['title'])
# position = data[0]['title']  # 职位
# salary
# experience
# area=
# edu=
# welfare
# company = soup.select('.tHeader.tHjob .in .cn .cname .catn')
# print(company[0])
