def wantGoHome(who = '메가스터디는'):  #<- 기본값을 정해주는 것 () 안에 아무것도 안나왔을 때 나오게 하는 것
    print(f'{who}집에 가고 싶다')
    print('빨리ㅋㅋ')



# 두 수를 받았을 때 큰 숫자 불러오기


def whichIsBigger(a,b):
    if a > b:
        print(f'{a}가 더 크네요!')
    else:
        print(f'{b}가 더 크네요!')


def Giving_100():
    return 100                 #결과값이 있다는 것 return이 없으면 결과값 없어

def abc(*coffee):
    return coffee[2]


# 제곱수를 돌려주는 함수
def Double(num):
    return num * num