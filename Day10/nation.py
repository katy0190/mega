import matplotlib.pyplot as plt
import numpy as np

file_path = 'visit'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print(content)

splitContent = content.split('\n')
nations = splitContent[0].split('\t')
visitNum = splitContent[1].split('\t')
newVistNum = visitNum[0:20]
print(nations)
print(newVistNum)

y = np.array(newVistNum)

plt.rc('font', family='Malgun Gothic')  #한글로 바꿔줘

plt.pie(y, labels=nations)
plt.show()