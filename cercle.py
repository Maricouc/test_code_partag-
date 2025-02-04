
import numpy as np


class Circle:
    def __init__(self, radius, center, point):
        self.radius = radius
        self.center = center
        self.point = point

    def calcul_area(self):
        self.area = np.pi*self.radius**2
        return self.area

    def calcul_perimeter(self):
        self.perimeter = 2*np.pi*self.radius
        return self.perimeter

    def calcul_out(self):
        if np.sqrt((self.center[0]-self.point[0])**2+(self.center[1]-self.point[1])**2) > self.radius:
            print("Le point est à l'extérieur du cercle")
        else:
            print("Le point est à l'intérieur du cercle")


mon_cercle = Circle(3, [0, 0], [5, 6])

a = mon_cercle.calcul_area()
print(a)
mon_cercle.calcul_out()
