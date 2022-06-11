class Food:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def get_nutrition(self):
        return self.energy
