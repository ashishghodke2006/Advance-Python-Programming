class Vehicle :
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def drive(self):
        print(self.brand,self.price)
v1=Vehicle("Maruti",120000)   

v1.drive()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Ashish", 50000)
e2 = Employee("Aashpreet", 60000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)

#output
#Maruti 120000
# Ashish 50000
# Aashpreet 60000