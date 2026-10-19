class Automobile:
    def __init__(self, type, brand, color, fuel_type):
        self.type = type
        self.brand = brand
        self.color = color
        self.fuel_type = fuel_type

    def display_information(self):
        return f"{self.type} {self.brand} {self.color}"
    
    def fuel_Type(self):
        return f"{self.type} {self.brand} is fuel type with {self.fuel_type}."


class Car(Automobile):
    def __init__(self, type, brand, color, fuel_type):
        super().__init__(type, brand, color, fuel_type)
        

class Bike(Automobile):
    def __init__(self, type, brand, color, fuel_type):
        super().__init__(type, brand, color, fuel_type)


car1 = Car("Sedan", "Toyota", "Red", "Petrol")
bike1 = Bike("Sports Bike", "Yamaha", "Blue", "EV")

print(car1.display_information())
print(car1.fuel_Type())   

print(bike1.display_information())
print(bike1.fuel_Type())