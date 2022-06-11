from animal import Animal


class Dog(Animal):
    def __init__(self, name: str, price: float):
        super().__init__(name)
        self.price: float = price

    def bark(self):
        print(f"{self.name}: Gua gua")

    def __str__(self):
        return self.name
