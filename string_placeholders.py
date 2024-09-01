# placeholders in strings

name = "Jake"
print(name + " is 15 years old")

'''
Specify a stirng placeholder
using %s to say what type it is
and where it should go in the sentence
in this code the place holder string
always appears at the beginning of the sentence
but it can be whereever you place the %s in the string
'''
sent = "%s is 15 years old"
print(sent%name)
print(sent%"Adam")

'''
variable with the placeholder %s - % - what you want the placeholder to be!
Using a single placeholder string
It's a nice neat way to include variables within strings
'''
print(sent%"Kate")
# using two placeholder strings
sent2 = "%s likes programming in %s"
print(sent2%("Adam","Python"))

'''
using placeholder strings is a lot cleaner then doing
it this way
'''
name3 = "Adam"
programming3 = "python"
sent3 = "likes programming in"
print (name3 + " " + sent3 + " " + programming3)

# place holders in strings with integers
# %d is for integers
sent4 = "%s is %d years old"
print(sent4%("Adam",43))

sent5 = sent4%("Timmy",41)
print(sent5)

'''
In Python you can only concatenate string to string
you cannot concatinate string to int
the solution is to convert to int to a string type with the str() method
but you cannot concatinate string and int types without this conversion to string
'''
try:
    print("Adam" + 15) # will throw an error
except:
    print("In Python you can only concatenate str (not int) to str")

# end of code
