# 1. 정수 N을 입력 받아
# - 0 미만 이면 cold, indoor 출력
# - 0~40 이면 moderate, outdoor 출력
# - 40 이상 이면 hot, indoor 출력

a = int(input('입력하세요 : '))

if a < 0:
    print("cold, indoor")

elif a > 0 and a < 40:          # elif 0 < a < 40:
    print("moderate, outdoor")

else:
    print("hot, indoor")


# 에어컨 프로그램 작성
#
# 2. 두 양의 정수 N, M을 입력 받아, 두 수의 제곱 관계
# - 제곱 관계가 아니면 None을 출력
# - 4 2 입력 -> 2 * 2 = 4
# - 3 9 입력 -> 3 * 3 = 9
# - 4 3 입력 -> none

n,m = int(input('두 수를 입력하세요. :').split())

if n % m == 0:
    print(f"{n} * {n} = {m}")

elif m % n == 0:
    print(f"{m} * {m} = {n}")

else:
    print('none')


#
# 3. 5개의 정수를 입력 받아서, 양의 정수들의 합 구하기
#
# - 2 5 -12 0 32 입력하면 -> 39
# - 0 -1 -3 -5 -7 입력하면 -> 0

a = int(input('숫자를 입력하세요'))
b = int(input('숫자를 입력하세요'))
c = int(input('숫자를 입력하세요'))
d = int(input('숫자를 입력하세요'))
e = int(input('숫자를 입력하세요'))

total = 0

if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
if d > 0:
    total = total + d
if e > 0:
    total = total + e

print(f"양의 정수의 누적은 {total}입니다.")
