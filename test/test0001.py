# stt = "1.5-2.5万"
# if stt.find('万') != -1:
#     print('包含万')
# a = stt.split('-')[1][:-1]
# print(a, type(a))
#
# b = (float(a) + 2.0) / 2
# print(b)
# dd = "北京朝阳"
# if dd.find('-') != -1:
#     print('ok')
# else:
#     print("不包含-")
# for i in range(2):
#     if i == 1:
#         list1 = [1, 2, 3, 4, 5]
#     else:
#         list2 = [3, 4, 5, 6, 7, 8]
#
# print(list1)

# dic = {'剧情': 11, '犯罪': 10, '动作': 8, '爱情': 3, '喜剧': 2, '冒险': 2, '悬疑': 2, '惊悚': 2, '奇幻': 1}
# #  通过list将字典中的keys和values转化为列表
# keys = list(dic.keys())
# print(list(dic.keys()), "--------------")
# print(list(dic.values()), "--------------")
#
# values = list(dic.values())
# # 结果输出
# print("keys列表为：", end='')
# print(keys)
# print("values列表为：", end='')
# print(values)

aa = "('成都',)"
dd = aa.replace("('", "").replace("',)", "")
print(dd)

dict1 = {'上海': 11, '长沙': 5, '杭州': 2, '苏州': 3, '深圳': 10, '广州': 4, '北京': 1, '西安': 2, '东莞': 1, '南京': 2, '昆明': 2, '济南': 1}
print(dict1.keys())




