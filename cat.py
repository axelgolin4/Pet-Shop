from animal import Animal


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def meow(self):
        return f"{self.name}: meooooooooow"
