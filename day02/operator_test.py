# Operator
# 연산자는 타겟을 지지고 볶는 것
# 할당 연산자 [=, *=, +=, -=]
a = 1
a += 1 # a에 재할당
a -= 1
a *= 1

# 수리연산자 [+, -, *, /(몫), %(나머지)]
b = 10 / 3 #b 몫          ... 3.33333333
b = 10 % 3 #b 나머지       ... 1

print(b)

# 비교 연산자 [<,>, <=, >= ==, !=]
# 무조건 결과값이 True or False(Boolean Type)
x = 1
y = 2
print(x == y) # == 같니? != 다르니?
print(x != y) # oo 다름
print(x > y)
print(x < y)

# 논리 연산자 및 우선순위 연산자 [and, or , not, ()]
bitcoin = 100
doge = 20
print(bitcoin > 0 and doge < 200)
print((bitcoin > 0 and bitcoin < 200) or doge > 100)
print(not(bitcoin < 0))

# in 연산자 [리스트]
x = ['mega','study','shinchon']
print('study' in x)             # x안에 스터디가 있니?




