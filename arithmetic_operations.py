# arithmetic operations with numbers

# declare integers
age1 = 12
age2 = 18

print(age1+age2) # addition
print(age1-age2) # subtraction
print(age1*age2) # multiplication
print(age1/age2) # division
print(age1%age2) # mod - gets the remainder
print(age2%age1) # mod - gets the remainder

# arithmetic operations with strings

sent1 = "today was a wonderful day" # string data type
print(sent1)

firstname = "Adam " # includes a space at the end of the string
lastname = "Duke"

print(firstname + lastname) # add or concatinate the strings together

print("Hi " * 10) # you can multiple a string and an integer like this

'''
However you cannot use subtraction, divide or mod on strings
'''

try:
    subtract = firstname - lastname
except:
    print("Error you cannot subtract strings!")

try:
    divide = firstname / lastname
except:
    print("Error you cannot divide strings!")

try:
    mod = firstname % lastname
except:
    print("Error you cannot mod strings!")

sent2 = "Adam was programming in Python!"

# string slicing
# python does not count the ending position
print (sent2[0]) # expected output is A
print (sent2[0:4]) # expected output is Adam
print (sent2[0:]) # expected output in Adam was programming in Phython!
print (sent2[:3]) # expected output is Ada
print (sent2[:-1]) # expected output is Adam was programming in Phython

# end of code
