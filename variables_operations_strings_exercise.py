# variables, operations and strings exercises

'''
Write a script that adds 15 and 30 and divides the sum by 2.
Print out the answer. 
'''
a = 15
b = 30
print((a+b)/2) # 22.5 is the expected output

'''
Initialize two variables and use arithmetic operators to add,
subtract, multiply, divide, and find the remainder. 
'''
a = 5
b = 10
print(a + b) # expected output is 15
print(a - b) # expected output is -5
print(a * b) # expected output is 50
print(a / b) # expected output is 0.5
print(a % b) # expected output is 5

'''
Create a variable called name and store your name in it as a string.
'''
name = "Adam"
print(name)

'''
Create three variables in one line and assign each one a different food item.
'''
a,b,c = "Apple","Orange","Pear"
print(a,b,c)

'''
Print out "Hello" ten times using arithmetic operators. 
'''
print("Hello "*10)

'''
Set your name and age variables in one line with multiple assignment 
'''
name,age = "Adam",43
print(name,age)

'''
Create two strings and then create a
third variable combining both of the two original strings. 
'''
a = "String1 "
b = "String2"
c = a + b
print(c)

'''
Create a string and print the fourth letter of the word. 
'''
a = "Hello"
print(a[3]) # expected output is o

'''
Create a string and print the letters from index 0 to 5.
'''
a = "Wonderful"
print(a[0:6]) # make sure to add one as the last index is not included

'''
Create a variable and print all the letters from the first index until the end.
'''
a = "Have a wonderful day today everyone!"
print(a[1:]) # first index meaning 1 rather than 0

# end of code
