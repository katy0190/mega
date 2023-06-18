# set은 집합이다.
# set특징 중복 안됨, 순서가 없음
# set 생성 및 초기화 방법

a = {2, 3, 4, 5}
b = set((7, 8, 9))
#print(a)
#print(b)

# 함수들
# add() 추가하기
a.add(0)
a.add(1)

# update() set을 추가하기
a.update(b)
print(a)

#remove() 값을 삭제하기

# union() set + set = new set
c = a.union(b)
print(c)