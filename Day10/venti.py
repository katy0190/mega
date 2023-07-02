class MenuItem():
    def __init__(self, name, image):
        self.name = name
        self.image = image


class coffee(MenuItem):
    def __init__(self, name, image, isIce, isHot):
        super().__init__(name, image)
        self.isIce = isIce
        self.isHot = isHot

class Juice(MenuItem):
    def __init__(self, name, image):
        super().__init__(name, image)
        self.isIce = True