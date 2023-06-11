a,b = input('두 수를 입력하세요. :').split()

if a > b:                              #if 순서는 지켜줘야 함
   print("앞의 수가 더 크네요!")

elif a == b:
   print("두 수가 같네요!")

elif a - 1 == b:
   print("앞의 수에서 하나 뺀 것이 뒤의 수네요.")

else:
   print("뒤의 수가 더 크네요!")

print("프로그램 종료합니다.")



###퀴즈
#a,b = input('두 수를 입력하세요. :').split()   ## split은 두수를 쪼개는거라 한개만 넣을 땐 아니야!!!!

#if a > b:
    #print(int(a) + int(b))

a = int(input('각도를 입력하세요. (0~180 사이) :'))

if a < 90:
    print("예각")

elif a == 90:
    print("직각")

elif a > 90 and a < 180:
    print("둔각")

elif a > 180:
    print("프로그램 고장납니다. 제대로 입력해주세요")

else:
    print("둔각")

###퀴즈2

a = int(input('숫자를 입력하세요.:'))

if a %2==1:
    print("홀수입니다.")

else:
    print("짝수입니다.")

###퀴즈3
#세 수중에서 가장 큰 수를 구하기
#조건 같은 수를 넣지는 않습니다.
# ex) 1 2 3 넣으면 3 가장 큰 수 입니다.

num1, num2, num3 = input("세 수를 입력하세요:").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

max = num1

if num2 > max:
    max = num2

if num3 > max:
    max = num3

print(f"가장 큰 수는 {max}이군요!")




year = int(input("연도를 입력하세요:"))
month = int(input("월을 입력하세요:"))

day = 31
if month in [4, 6, 9, 11]:
    day = 30

# 윤년 판단

isLeapYear = False
if year % 4 == 0:
    isLeapYear = True

if isLeapYear and month == 2:
    day = 29

elif not isLeapYear and month == 2:
    day = 28

print(f"해당 월의 일수는 {day}입니다.")




