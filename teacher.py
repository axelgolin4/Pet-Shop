from human import Human
from husky import Husky
from food import Food
from credit_error import CreditError
from animal import Animal


class Teacher(Human):
    def __init__(self, name: str):
        super().__init__(name)

    # def feed(self, animal: Husky, food: Food):
    #     print('--------------------------')
    #     print(f"Alimentar a {animal}")
    #     print(f"{self.name}: Haz un truco")
    #     animal.roll_over()
    #     print(f"{self.name}: *Dar comida*")
    #     animal.eat(food)
    #     print('--------------------------')

    def buy_dog(self, name: str, price: float) -> Animal:
        if price < 0:
            raise ValueError

        if self.money >= price:
            self.money -= price
            return Animal(name)
        else:
            raise ArithmeticError
