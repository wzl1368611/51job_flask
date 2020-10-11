# a = 12 / 5.0
# print(a)
x = ('1.5-2.5万/月',)
a = str(x)
print(a)
print(str(x).split('/')[0].replace("('", ""))
# sum = []
# count0 = 0
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# count6 = 0
# count7 = 0
# for i in data:
#     print(i, type(i))
#     avg = 0
#     i = str(i)
#     list = i.split('/')[0]
#     num = list.split('-')
#     if list.exists('千'):
#         avg = (int(num[0]) + int(num[1][:-1])) / 20.0
#     else:
#         avg = (int(num[0]) + int(num[1][:-1])) / 2.0
#     if avg < 0.6:
#         count0 += 1
#     elif 0.6 < avg < 0.8:
#         count1 += 1
#     elif 0.8 < avg < 1.2:
#         count2 += 1
#     elif 1.2 < avg < 1.5:
#         count3 += 1
#     elif 1.5 < avg < 2:
#         count4 += 1
#     elif 2 < avg < 3:
#         count5 += 1
#     elif 3 < avg < 4:
#         count6 += 1
#     elif avg > 4:
#         count7 += 1
# sum = [count0, count1, count2, count3, count4, count5, count6, count7]
