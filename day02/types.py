#Data Types ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
#프로그래밍 언어에서 두가지로 나뉨
# 1. 컴파일 언어 ex)아래 2번째 제외 모두
# - 데이터 타입을 미리 정함
# - dollar -> int dollar = 10 or String dollar = "10"
# - 하나라도 틀리면(컴파일 과정) 걸러짐


# 2. 인터프리터 언어 ex) python, javascript
# - 데이터 타입을 그 때 정함
# - 일단 돌리고 봄.


# 1. str (문자열)
a = "나는 문자열입니다"
print(type(a))

# 2. int (정수)
b = 123
print(type(b))

# 3. float (실수 mistake X)
c = 123.123
print(type(c))

# 4. list
d = [123, '4566', 12.35, [1,2,3]] #'' < 문자열로 바꿔주는 것
print(type(d))

# 5. dict
e = {'name':'katy', 'age':21, 'Language':['c','js','ts','java']}
print(type(e))

# 6. set 집합
f = {"apple", "banana", "pineapple", "apple"}
print(f)
