# Object Oriented Programming (OOP)

'''
Classes are the top level
Objects are the instance of a class
Person Class - Describes a Person
Person Instance - A Person
'''

'''
Class is like a duplication machine like a car making factory
Objects or instances are the cars that come out of the factory
'''

'''
A class
Object is an instance of that class
Object is the specific structure of behaviour (defined by the class)
So every instance of a class is an object
But the word object can be used more generally to refer to other
things besides beyond class instances
'''

# create the class
# you can use pass to make an empty working class

class Person: # creates a person class

    # function of this class
    # self refers to the current instance that you have
    # self tells the class which object or instance to apply
    # this function to
    def getName(self):
        print("Adam")

    def getAge(self):
        print(43)
    
# create an object or an instance of the person class
p = Person() # now P is an instance of the Person class
print(p) # Person object at this memory location

# call a function of this object or instance of the person class

# this is better because it's a more typical and clearer way 
# to call a method in Python.
# it uses the objects short hand syntax and is easier to understand
# using sytantic sugar make OOP more intuitive while still having
# the same outcome and the long hand version of the code
p.getName() # short hand
Person.getName(p) # long hand

p.getAge() # short hand
Person.getAge(p) # long hand

# init function is called right when you created the object
# or instance of the class and it takes in the paramamters
# that you give it and assigns those to the variables in
# the class

class Person2():

    # the init function
    # passing in self, name and age
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # the getName function
    def getName(self):
        print("Your name is: " + self.name)

    # the getAge function
    def getAge(self):
        print("Your age is: " + str(self.age))

 # create an instance of Person2
 # pass in the name and age into the Person2 class init function
 # the init function of the class takes in any parameters you need
 # once the object or instance is created of the class
person_adam = Person2("Adam",44)

# call the getName and getAge functions of the Person2 class
# for this instance call person_adam
person_adam.getName()
person_adam.getAge()

# end of code
