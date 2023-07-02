class Animal:
    def __init__(self, name):
        self.name = name

    def sounding(self):
        pass


class Lion(Animal):
    def sounding(self):
        print("어흥")


class Monkey(Animal):
    def sounding(self):
        print("우끼끼")
