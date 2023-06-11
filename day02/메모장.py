#1월 31일
#2월 28일 or 29일
#3월 ....
#년도 입력하세요.
#몇월을 입력하세요.
#그렇다면 해당 월의 일수는 31 or 28 or 29 or 30



year = int(input ("연도를 입력하세요:"))
month = int(input ("월을 입력하세요:"))


day = 31
if month in [4, 6, 9, 11]:
    day = 30

#윤년 판단

isLeapYear = False
if year % 4 == 0:
    isLeapYear = True

if isLeapYear and month == 2:
    day = 29

elif not isLeapYear and month == 2:
    day = 28

print(f"해당 월의 일수는 {day}입니다.")