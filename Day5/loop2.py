#for vs while
#break, continue
#반목문을 컨트롤 하기 위한 예약어로 보면 됨


num = int(input("숫자를 입력해주세요."))
for i in range(100):
    if(i == num):   # num이 i 와 같으면 멈춰죠
        break
    print(i)


#continue : 다시 시작해 아래 있는 코드 무시하고 !

for i in range(100):
    if(i == 10):  # 10제외하고 나머지 다 나옴
        continue
    print(i)

for i in range(100):
    if(i % 2 != 0):  # 10제외하고 나머지 다 나옴
     print(i)


# 3 5 배수 구하기

for i in range(100):
    if (i % 3 == 0):
        print(i)
    elif(i % 5 == 0):
        print(i)
    else:
        continue



