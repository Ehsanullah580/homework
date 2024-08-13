# Add a method called greet to the Person class that prints a greeting message including the person's name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def greeting(self):
        print(f"Hello, How are you {self.name}")
    
ahmad = Person("Ahmad", 18)
ahmad.greeting()