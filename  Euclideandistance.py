import math

class Euclidean:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def calculatedistance(self, x2, y2):
        distance = math.sqrt((x2 - self.x1) ** 2 + (y2 - self.y1) ** 2)
        return distance


x1 = int(input('Enter the x1 coordinate:-'))
x2 = int(input('Enter the x2 coordinate:-'))
y1 = int(input('Enter the y1 coordinate:-'))
y2 = int(input('Enter the y2 coordinate:-'))
point1 = Euclidean(x1, y1)
distance = point1.calculatedistance(x2, y2)
print("The Euclidean distance between the points is:-", distance)
