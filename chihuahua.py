from dog import Dog


class Chihuahua(Dog):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def dance(self):
        print(f"{self.name}: Estoy bailando")
