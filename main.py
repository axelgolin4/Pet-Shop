from chihuahua import Chihuahua
from dog import Dog
from human import Human
from husky import Husky
from student import Student
from food import Food
from teacher import Teacher
from credit_error import CreditError


pets: list[Dog] = [
    Husky('Goku', 25.50),
    Chihuahua('Bell', 55.00),
    Chihuahua('Moly', 50.50)
]

people: list[Human] = [
    Student('Bryan', 21),
    Student('Paolo', 22),
    Teacher('Jorge')
]

for dog in pets:
    dog.bark()

# 1 - Los parámetros deben coincidir o ser más abstractos
# for dog in pets:
#     people[0].feed(dog, Food('Concentrado', 10))
#     people[2].feed(dog, Food('Sobras de la cena', 5))

# 2 - El tipo de retorno debe coincidir o ser más específico
# print('--------------------------')
# print('Comprar perro')
# animal = people[1].buy_dog('Firulais', 1.00)
# animal.bark()
# pets.append(animal)
# print('--------------------------')
# print('--------------------------')
# print('Comprar perro')
# animal = people[2].buy_dog('Hachi', 1.00)
# animal.bark()
# pets.append(animal)
# print('--------------------------')

# 3 - Se deben arrojar el mismo tipo de excepciones
# try:
#     print('--------------------------')
#     print('Comprar con problemas')
#     people[0].buy_dog('Doky', 1000000)
#     print('--------------------------')
# except CreditError as err:
#     print(err)
#
# try:
#     print('--------------------------')
#     print('Comprar con problemas')
#     people[2].buy_dog('Doky', 1000000)
#     print('--------------------------')
# except CreditError as err:
#     print(err)

# 4 - Una subclase no debe fortalecer las condiciones previas
# print('--------------------------')
# print('Comprar con condiciones')
# dog = people[1].buy_dog('Doky', -10)
# dog.bark()
# print('--------------------------')
#
# print('--------------------------')
# print('Comprar con condiciones')
# dog = people[2].buy_dog('Doky', -10)
# dog.spin()
# print('--------------------------')

# 5 - Una subclase no debe debilitar las condiciones posteriores
# people[0].feed(pets[0], Food('Concentrado', 10))
# people[2].feed(pets[1], Food('Sobras de la cena', 5))
