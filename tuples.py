# Tuples

# a tuple is an immutable list
# once created values cannot be altered, deleted or added

# tuple - cannot be changed once created
tup = ("Oranges","Apples","Bananas")
print(tup[0]) # accessed via the index
print(tup[0:2]) # slicing works just like a list

try:
    del(tup[0])
except:
    print("Tuple object does not support deletion")

try:
    tup[0] = "Pear"
except:
    print("Tuple object does not support editing / assignment")

# dictionary - key / value pairs that can be changed
dic = {"Oranges":"Orange","Apples":"Red","Pear":"Green"}
print(dic["Apples"]) # accessed via the key

# list - a list of strings or number that can be changes
lis = ["Oranges","Apples","Bananas"]
print(lis[0]) # accessed via the index

# just like lists tuples can be added together
tup2 = (12,14)
print(tup + tup2)

# you can delete an entire tuple with the del() statement
del(tup2)

tup3 = (1,2,3)
print(len(tup3)) # len() statement works in tuples too
print(tup3 * 3) # multiply still works like on a list or variable


# end of code
