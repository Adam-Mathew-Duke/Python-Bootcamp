# conditional statements
# if
# elif means else if
# else

# relational operations
# >= greater than or equal to
# <= less then or equal to
# == equal to
# != not equal to
# > greater than
# < less than

if (5 > 3): # expected true
    print("true")

if (3 < 2): # expected false
    print("true")
else:
    print("false")

age = 16

if (age < 13):
    print ("You are young")
elif (age >=13 and age < 18):
    print("You are an teenager")
else:
    print("You are an adult")

if (5 > 3 and 2 > 1): # if both conditions are true
    print("true")

if (5 > 3 or 2 < 1): # if one or more conditions are true
    print("true")

# end of code
