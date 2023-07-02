class MegaCoffee:
    # 변수, 속성, 명사화
    def __init__(self, location, th, coffee, sale):         # < 필수로 같이 써줘야 함
        self.location = location
        self.th = th
        self.coffee = coffee   #< 요스타일은 외워주기
        self.sale = sale         # self.sale = 0 으로 해줄 수도 있음 대신 이러면 oop test 에서 0을 지워줄 것

    def selling_signature(self):              #동사만들기
        self.sale = self.sale + 4000          #매출 누적해주기
        print("이게 시그니처가 팔리네;")

    def today_earning(self):
        if(self.sale < 15000):
            print(f"{self.sale}분발하세요.")
        else:
            print(f"{self.sale}입니다.👌")