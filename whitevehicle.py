#Define a class attribute “color” with a default value white. i.e., Every Vehicleshould be white.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = "white"  

    def vehicle_info(self):
        return f"Company: {self.make}\nModel: {self.model}\nColor: {self.color}\n"


vehicle1_company = input("Enter the company name of vehicle 1:-")
vehicle1_model = input("Enter model name of vehicle 1:-")
vehicle = Vehicle(vehicle1_company, vehicle1_model)

vehicle2_company = input("Enter the company name of vehicle 2:-")
vehicle2_model = input("Enter model name of vehicle 2:-")
vehicle2 = Vehicle(vehicle2_company, vehicle2_model)

vehicle3_company = input("Enter the company name of vehicle 3:-")
vehicle3_model = input("Enter model name of vehicle 3:-")
vehicle3 = Vehicle(vehicle3_company, vehicle3_model)


print(vehicle.vehicle_info())
print(vehicle2.vehicle_info())
print(vehicle3.vehicle_info())
