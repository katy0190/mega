# 반복문
# for 문

#for 변수 in range<함수(돌리고 싶은 횟수 만큼의 숫자)

for abc in range(100):
   print("고기")  #print 100개 출력

for abc in range(100):
   print(abc)  # 몇번째 인지 알려주는 애




# num = int(input("숫자를 입력해주세요: "))
for abc in range(num):
    print("메가스터디")  #print 100개 출력



#0부터 짝수만 출력해주세요.

num = int(input("숫자를 입력해주세요: "))

for abc in range(num):
    if(abc % 2 == 0):
     print(abc)



# 입력한 숫자의 합을 출력해 주세요.

num = int(input("숫자를 입력해주세요: "))
count = 0
for i in range(num+1):
    count = count + i       # count = count + 1 => count += 1 같은 것
print(count)


# 입력한 숫자의 합을 출력해 주세요. #가오스 공식?

num = int(input("숫자를 입력해주세요: "))

sum = (num * (num + 1)) / 2
print(sum)


# 5!은 120입니다??????

num = int(input("숫자를 입력해주세요: "))
factorial = 1

for i in range(num+1):
    if(i == 0):
        pass
    factorial = factorial * i


# 1~1000 의 숫자 중에서 입력한 숫자의 수의 배수들을 출력해주세요.
# 1. 숫자 입력
# ex) 3,6,9,12,15

num = int(input("숫자를 입력해주세요: "))

for i in range(1,100):







