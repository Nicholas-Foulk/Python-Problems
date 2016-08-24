##Animal is-a object
class Animal(object):
    pass
##Dog is-a subclass of Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name
## Person is-a object
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
## Employee is-a subclass of Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ##this allows us to run the __init__ of the parent class reliably.
        super(Employee, self).__init__(name)
        self.salary = salary
#Fish is-a object    
class Fish(object):
    pass
#Salmon is a subclass of fish
class Salmon(Fish):
    pass
#Halibut is a subclasss of fish
class Halibut(Fish):
    pass
### class is-a object
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

#we defined this on line 12
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
