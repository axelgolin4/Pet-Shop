from human import Human
from husky import Husky
from chihuahua import Chihuahua
from food import Food
from animal import Animal
from dog import Dog
from credit_error import CreditError


class Student(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def request_money(self):
        self.money += 10

    def feed(self, animal: Animal, food: Food):
        print('--------------------------')
        print(f"Alimentar a {animal}")
        print(f"{self.name}: Haz un truco")
        animal.spin()
        print(f"{self.name}: *Dar comida*")
        animal.eat(food)
        animal.sleep(8)
        print('--------------------------')

    def buy_dog(self, name: str, price: float) -> Husky:
        if self.money >= price:
            self.money -= price
            return Husky(name, price)
        else:
            raise CreditError
