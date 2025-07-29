#creating a class and giving it some attributes

class Dog():
    def __init__(self,name,age):   #method or constructor
        self.name = name        #Atrributes
        self.age = age
    
    def bark(self):             #Other methods or functions
        print(self.name.title() + " is barking")
        

my_dog = Dog("Alex" , 5)
my_dog.bark()