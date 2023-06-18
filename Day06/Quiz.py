set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. set1과 set2의 합집합을 출력하세요.

print(set1.union(set2))

# 2. set1과 set2의 교집합을 출력하세요.

print(set1 & set2)

# 3. set1에서 set2를 제외한 차집함을 출력하세요.

print(set1 - set2)

# 4. set1과 set2의 대칭 차집합을 출력하세요.

print(set1 ^ set2)


# 5. set1과 set2의 합집함을 새로운 변수에 할당한 후 해당 변수를 출력하세요.

set3 = set1.union(set2)
print(set3)