class SubwayMenu():
    def __init__(self, name, image, kcal, price):
        self.name = name
        self.image = image
        self.kcal = kcal
        self.price = price


class Sandwich(SubwayMenu):
    def __init__(self, name, image, kcal, price, new):
        super().__init__(name, image, kcal, price)
        self.new = new




