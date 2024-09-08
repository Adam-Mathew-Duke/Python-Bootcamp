# inheritance

'''
For example:
Class Person
    Class Female - top level class
        Class Children - child class that inherits the parent class 
        Class Teenager - child class that inherits the parent class
        Class Adult - child class that inherits the parent class
'''

class Parent():

    def __init__(self):
        print("This is the parent class init")

    def parentFunction(self):
        print("This is the parent class function")

# the class Children inherits the top level parent class
# for example a mum has blue eyes and so does the child
class Children(Parent):

    def __init__(self):
        print("This is the Children class")

    def childrenFunction(self):
        print("This is the Children class function")

parent_instance = Parent()
parent_instance.parentFunction()

children_instance = Children()
children_instance.childrenFunction()

'''
when you inherit from the Parent class you also get
all the functions of the Parent class too.
so with inheritance you get all the functions of the 
parent class and all the functions of the child class
'''
children_instance.parentFunction()

'''
For example every person (class)
Parent Class: Eats, sleeps and has an name and an age
Children Class: Gender is different for each instance of
the children class. Eye color is different, height is different,
age is different. Type of sleep is different, name is different.
Parent Class: Every person has a name (not specific)
Children Class: This instance of the children class has a 
specific name like Kate.
'''

'''
Parent Class - defines what traits a person has
Children Class - inherits the traits from the parent class
and can change them. e.g. Inherites eyes from the parent class
but changes them to blue for the children instance
'''

'''
Overriding functions if the Parent Class and the Children class
have the same methods like GetName how do I telll Python which
function I want to call?
'''

class Parent2():

    def __init__(self):
        pass

    def test(self):
        print("Parent2 Class")

class Child2(Parent2):

    def __init__(self):
        pass

    # In Python if you re-initalise the function
    # in the inherited child class it will replace it
    # it has the same name as in the parent class so 
    # it will be overwritten as long as it has the same name
    # whatever code we put in the child class will be used
    # instead of the code in the parent class
    # if there is not function in the child class called test
    # when Python will use the function in the parent class
    # instead
    def test(self):
        print("Child2 Class")

parent_instance2 = Parent2()
parent_instance2.test()

Child_instance2 = Child2()
Child_instance2.test()

# end of code
