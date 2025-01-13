class Car: 
    def __init__(self, make, year, color):
        self.make = make
        self.year = year
        self.color = color
    
    def carDescription(self):
        return f'{self.make} {self.year} {self.color}'
    


newCar = Car('Toyota', 2007, 'Blue')
print(newCar.carDescription())
