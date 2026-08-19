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