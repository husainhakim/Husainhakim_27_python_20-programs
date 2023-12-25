class Car:
    def __init__(self, make, model, year, color, mileage, owner_name):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.owner_name = owner_name

    def display_details(self):
        print(f"Car Details:\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n"
              f"Mileage: {self.mileage}\n"
              f"Owner: {self.owner_name}")


mycar = Car("Mahindra", "Thar", 2010, "Black", "30,000 miles", "Husain hakim")


mycar.display_details()
