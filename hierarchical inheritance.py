class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Vehicle Details:-\n"
              f"Company: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
       

    def display_details(self):
        super().display_details()
       


class Truck(Vehicle):
    def __init__(self, make, model, year, weightcapacity):
        super().__init__(make, model, year)
        self.weightcapacity = weightcapacity

    def display_details(self):
        super().display_details()
        print(f"Type: Truck\nPayload Capacity: {self.weightcapacity} tons")


class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.typebike = bike_type

    def display_details(self):
        super().display_details()
        print(f"Type: Bike\nBike Type: {self.typebike}")


car = Car("Mahindra", "Thar", 2010, 4)
truck = Truck(" Honda", "Ridgeline", 2023, 2.5)
bike = Bike("Royal Enfield", "Continental GT 650", 2018, "Sport")


car.display_details()
print("\n")
truck.display_details()
print("\n")
bike.display_details()
