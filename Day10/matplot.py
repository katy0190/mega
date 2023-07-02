import matplotlib.pyplot as plt
import numpy as np
#
# f = np.genfromtxt(fname=".txt")
#
# # x = np.linspace(-5, 2 * np.pi, 10)
# # y = np.sin(x)
# #
# # fig, ax = plt.subplots()
# # ax.bar(x, y)
# # plt.show()
#
#
# x = np.array([0, 5, 10])
# y = np.array([0, 10, 100])
#
#
# print(x, y)
#
#
# plt.plot(x, y)
# plt.show()

file_path = 'price'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print(content)

                                           # 메모장에서 replace를 사용하여 시도별과 전국을 없앤다.
                                           # onlyNumberContent = content.replace('시도별', '').replace('전국', '')


# 윗줄과 아래줄을 구분하기  #/n 줄바꿈

splitContent = content.split('\n')

yearsList = splitContent[0].split('\t')
priceList = splitContent[1].split('\t')

x = np.array(yearsList)
y = np.array(priceList)

plt.bar(x, y)
plt.show()




