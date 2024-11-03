from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can Walk and Run")
class Snake(Animal):
    def move(self):
        print("I can Crawl")
class Dog(Animal):
    def move(self):
        print("I can Bark")
class Lion(Animal):
    def move(self):
        print("I can Roar")

r = Human()
r.move()
r = Snake()
r.move()
r = Dog()
r.move()
r = Lion()
r.move()