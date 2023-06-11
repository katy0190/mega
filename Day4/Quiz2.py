# 여러분은 얼죽아 더죽아 입니다.
# 1. 현재 가지고 있는 용돈을 입력하세요.
# 2. 아아 가격이 얼마인지 입력하세요
# 3. 몇개의 아아를 구매 가능한지, 잔돈 얼마를 받나요?


a = int(input('현재 가지고 있는 돈을 입력하세요. : '))
b = int(input('아아 가격이 얼마인가요? : '))

money = int((a // b))
coffee = int((a % b))

print(f"{money}개의 아아를 구매 가능하고, 잔돈 {coffee}를 받습니다.")

# 여러분은 얼죽아 더죽아 입니다.
# 1. 현재 가지고 있는 용돈을 입력하세요.
# 2. 아아, 라떼, 디카페인을 가격이 얼마인지 입력하세요.
# 3. 원하는 커피를 선택을 하고(1.아아 2.라떼 3.디카페인)
# 4. 몇개의 라떼를 구매 가능한지, 잔돈 얼마를 받나요?

money = int(input('현재 가지고 있는 돈을 입력하세요. : '))
ameri = int(input('아아 가격이 얼마인가요? : '))
latte = int(input('라떼 가격이 얼마인가요? : '))
decaffein = int(input('디카페인 가격이 얼마인가요? : '))

select = input('커피를 선택해주세요.(1.아아 2.라떼 3.디카페인) : ')

menuName = {
    '1' : '아아',
    '2' : '라떼',
    '3' : '디카페인',
}


menuPrice = {
    '1': ameri,
    '2': latte,
    '3': decaffein,
         }

count = int(money // menuPrice[select])
rest = int(money % menuPrice[select])

print(f"{menuName[select]} 구입 가능 개수는 {count} 잔돈은 {rest} 입니다.")