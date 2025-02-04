
class Car:
    def __init__(self, make, model, year): # pas obligatoire
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def start_engine(self):
        print(f"Le {self.year} {self.make} {self.model} démarre.")

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"La voiture a une vitesse de {self.speed} kmh.")

    def brake(self, speed_decrease):
        self.speed = max(0, self.speed - speed_decrease)


my_car = Car("Honda", "Civic", 2021)
friends_car = Car("Ford", "Mustang", 2020)

my_car.start_engine()
print(f"Ma voiture est une {my_car.year} {my_car.make} {my_car.model}.")

my_car.accelerate(30)
my_car.brake(10)

friends_car.start_engine()
friends_car.accelerate(50)
