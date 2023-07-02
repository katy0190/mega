#class = 변수 and 함수
# 변수(속성)
# 함수(동작)
class Coffee:
    def __init__(self, name, price, isIce):
        self.name = name
        self.price = price
        self.isIce = isIce

# 관리자 클래스 만들기
class Manager:
    def __init__(self, name):
        self.name = name
    def registerCoffee(self, coffee, adminPage):
        adminPage.menu.append(coffee)


    # 관리자 페이지 만들기
class AdminPage:
    def __init__(self):
    #   self.admins = []  #이 안에 그 담당자가 있는지 아닌지 확인
        self.menu = []    #리스트 형식으로 등록

    # def showAdmins(self):
    #     for i in self.admins:
    #         print(i)              #관리자를 모두 보여주세요

    def showCoffees(self):
        for i in self.menu:      #반복문을 통해
            print(i)             #커피를 모두 보여주세요