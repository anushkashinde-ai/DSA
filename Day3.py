# Single Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()

obj.sound()
obj.bark()




# 2. Method Overriding (Runtime Polymorphism)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Dog()
a.sound()

a = Cat()
a.sound()


# 3. Multilevel Inheritance
class Grandfather:
    def house(self):
        print("Grandfather's House")

class Father(Grandfather):
    def car(self):
        print("Father's Car")

class Son(Father):
    def bike(self):
        print("Son's Bike")

obj = Son()

obj.house()
obj.car()
obj.bike()




# 4. Multiple Inheritance
class Father:
    def money(self):
        print("Father's Money")

class Mother:
    def jewelry(self):
        print("Mother's Jewelry")

class Child(Father, Mother):
    def toys(self):
        print("Child's Toys")

obj = Child()

obj.money()
obj.jewelry()
obj.toys()



# 5. Hierarchical Inheritance
class Parent:
    def property(self):
        print("Parent Property")

class Son(Parent):
    pass

class Daughter(Parent):
    pass

s = Son()
d = Daughter()

s.property()
d.property()



# 6. super() keyword
class Person:
    def __init__(self):
        print("Person Constructor")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student Constructor")

obj = Student()


# 7. Polymorphism Example
class Bird:
    def fly(self):
        print("Bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")

birds = [Sparrow(), Ostrich()]

for b in birds:
    b.fly()