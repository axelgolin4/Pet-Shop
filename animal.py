from food import Food


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.energy: int = 50

    def spin(self):
        print(f"{self.name}: *Empieza a girar*")

    def sleep(self, hours: int):
        print(f"{self.name}: Voy a dormir")
        self.energy = min(100, self.energy + (hours * 10))

    def eat(self, food: Food):
        self.energy = min(100, self.energy + food.get_nutrition())
