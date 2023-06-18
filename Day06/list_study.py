# List

# 생성 하는 방법
[]  #옛날 방식 list()


# 초기화 하는 방법

# 아래에 a b 를 datatype 이라고 함 > object class 라고도 함
a = list(range(10))           #자동으로 0부터 9까지 할당이 됨
a.append(12345)               #리스트에 도움이 되는 함수

# upper는 대문자로 바꿔 줌
b = 'mega'
print(b.upper())              #문자열을 지지고 볶는 함수


b = [1,'2',3,True,5[[[[]]]]] #리스트 안에 리스트를 계속 넣을 수도 있음. 문자, 숫자, True 다 됨

c = list('hello world!')  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!'] 이렇게 나옴

print(c)


# 주로 사용하는 method
# append(123) 맨 뒤에 123을 추가해 주는 것
# pop() 맨 뒤에서 빼는 것 ()안에 빼는 걸 넣어줄 필욘 없음 어차피 맨 뒤에서 빼는 거니까
# insert(2, 500) 어디에 넣고 싶은 값을 넣어 주는 것 ex) 2번째에 500을 넣는다
# remove(30) 30을 지운다
# index(3) 3번째 있는 값을 가져온다.
# count(5) 5인 숫자를 몇개인지 알려준다.
# reverse() 리스트를 거꾸로 바꾼다.
# sort() 정렬 👍👍👍 sort(reverse=True) 역정렬
# Clear() 클리어함


# 0 ~ 1000 짝수들만 있는 리스트를 만드시오.

a = list(range(1001))

for i in a:
    if (i % 2 != 0):  #홀수라면
        a.remove(i)   #나가
print(a)

#인덱싱
print(b[0])

numbers = [1, 2, 3, 4, 5]

# 1. 리스트의 첫 번째 요소를 출력하세요.

print(numbers[0])

# 2. 리스트의 마지막 요소를 출력하세요.

print(numbers[4]) # -1도 가능 역주행

# 3. 리스트의 두번째와 세번째 요소를 슬라이싱하여 출력하세요.

print(numbers[1:3])  # 끝은 포함 아님 앞을

# 4. 리스트의 모든 요소의 합을 계산하여 출력하세요.
# 1 for문
sum1 = 0
for i in numbers:
    sum1 = sum1 + i
print(sum1)

# 2 sum 이라는 내장 함수 이용

print(sum(numbers))

# 5. 리스트를 내림차순으로 정렬한 결과를 출력하세요.

numbers.sort(reverse=True)
print(numbers)

# 6. 리스트에 숫자 6을 추가한 후 리스트를 출력하세요.

numbers.sort()
numbers.append(6)
print(numbers)










