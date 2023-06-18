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


