# built in functions in Python

# abs() takes any positive or negative number and makes it positive
print(abs(34)) # 34
print(abs(-34)) # 34

# bool() if the number is 0 it will return false else return true
print(bool(0)) # 0 returns true
print(bool(None)) # true None is the same as 0
print(bool(1)) # 1 returns false
print(bool(100)) # 100 returns false
print(bool(-50)) # -50 returns false

# dir() directory will list all the functions for the data type
print(dir(1)) # lists all methods for integers in Python

# help() prints out help for a function in Python
# takes in a function name
sent = "Hello"
help(sent.upper) # use the function and no () is needed
help(sent.split) # use the function and no () is needed

# eval() runs single line Python code from a string
sent = "print('Hi')"
eval(sent)

# exec() runs multiline Python code from a string
exec(sent)

# convert between different data types in Python
# str()
# int()
# float()
a = 1
print(str(a))
print(int(a))
print(float(a))

# end of code
