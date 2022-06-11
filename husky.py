from dog import Dog
from food import Food


class Husky(Dog):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def roll_over(self):
        print(f"{self.name}: Estoy girando")
