from dog import Dog
from food import Food
from credit_error import CreditError


class Human:
    def __init__(self, name: str):
        self.name = name
        self.money = 100

    def feed(self, animal: Dog, food: Food):
        print('--------------------------')
        print(f"Alimentar a {animal}")
        print(f"{self.name}: *Dar comida*")
        animal.eat(food)
        animal.sleep(8)
        print('--------------------------')

    def buy_dog(self, name: str, price: float) -> Dog:
        if self.money >= price:
            self.money -= price
            return Dog(name, price)
        else:
            raise CreditError
