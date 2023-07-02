# 강아지 클래스

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):

    def __init__(self, name, age, cutting):
        super().__init__(name, age)
        self.cutting = cutting
    def barking(self):
        print("멍멍")


class Cat(Animal):

    def meowing(self):
        print("야옹")