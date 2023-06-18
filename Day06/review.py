import math

num1 = int(input("첫 번째 정수를 입력하세요:"))
num2 = int(input("두 번째 정수를 입력하세요:"))

a = math.gcd(num1,num2)   #최대 공약수 구하기
print(a)