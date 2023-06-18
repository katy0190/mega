#1.양의 정수 하나 입력 받고, 그 정수의 약수를 출력하는 프로그램
# ex) 15 -> 1 3 5 15 프로그램 만드시오
# ex) 18 -> 1 2 3 6 9 18 프로그램 만드시오

num = int(input("숫자를 입력하세요:"))
start = 1

while start < num:
    if(num % start == 0):
        print(start)
    start = start + 1


#2. 하나의 정수 n을 반복해서 입력받고, n의 합을 출력하는 프로그램
# 숫자 0을 입력 하면 종료됨
# ex) 5 1 3 2 0 => 11
# ex) 2 3 0 => 5
# ex) 1 2 3 10 23 124 0 => 163

num = int(input("숫자 넣어주세요:"))
sum = 0
while num != 0: #0이 아니면  == 같다 != 다르다
    sum = sum + num
    num = int(input("숫자 아무거나 입력하시오:"))
print(f"누적된 합은 {sum}입니다.")

########2번 문제 다른 방식으로 써보기##########

sum = 0
while True:
    num = int(input("숫자입력:"))
    if(num == 0):           # 넣어준 숫자가 0이면   <->    if(num != 0):
        break               # 멈춰                <->    continue
    sum = sum + num         # 아니면 누적해서 더 해줘
print(sum)


# 정수를 입력 하였을 때, 각 자리의 수의 합을 구하시오 0부터~10000
# ex) 1234 => 1+2+3+4 = 10
# ex) 333 = > 3+3+3 = 9

num = int(input("정수 입력"))
sum = 0
start = 10000
while True:
    sum = sum + num / start
    num = num / start
    start = start / 10 #1000으로 변경
    if(start == 0):  #0이 되면 끝내주세요
        break





