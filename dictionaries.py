# dictionaries

'''
List is a list of items created with ("1","2","3")
dictionary is a set of keys and values created with {"Key":value}
'''

# Create a dictionary of students names and ages
students = {"Bob":12,"Rachel":13,"Emily":15}

# access a value in the dictionary by using it's key
print(students["Rachel"]) # expected output is 13

# update Rachel's age in the student dictionary
students["Rachel"] = 14
print(students["Rachel"]) # expected output is 14

# remove the key / value pair from the dictionary
del students["Emily"]
print(students)

# length fuction works on dictionaries
print(len(students)) # there are 2 keys/value pairs in the dictionary

# end of code
