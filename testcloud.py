import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图：数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

conn = sqlite3.connect('job2.db')
cursor = conn.cursor()
sql = 'select task from job_info'
data = cursor.execute(sql)
text = ""
for item in data:
    print(type(item), len(item))
    text = text + item[0]
    # print(item[0])
# print(text)
# print(text, '------------')
conn.commit()
cursor.close()
conn.close()
cut = jieba.cut(text)
string = " ".join(cut)
print(string)
img = Image.open('static/img/tree.jpg')
# static\assets\img
img_array = np.array(img)  # 将图片转化成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='msyh.ttc',
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

# plt.show()  # 显示生成的词云图片
plt.savefig('static/img/task.jpg', dpi=500)
