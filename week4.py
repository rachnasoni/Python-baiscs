#
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
        
car = Vehicle(134,44 )
print(car.max_speed, car.mileage)

#
class Vehicle:
    pass

#
class Vehicle:

    def __init__(self, name, max_speed, mileage):                
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

#
class vehicle:
	def __init__(self,name ,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self):
		self.capacity = 100
		
class bus(vehicle):
	#method ovverride...
	def seating_capacity(self):
		self.capacity = 50
		print(f'the seating_capacity of {self.name} is {self.capacity} passanger')
b = bus("bus",45,45)
b.seating_capacity()

#
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 13, 96)
print("Total Bus fare is:", School_bus.fare()) 

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 13, 96)
print("Total Bus fare is:", School_bus.fare())

#
