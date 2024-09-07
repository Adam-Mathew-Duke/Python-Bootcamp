# for loops

list1 = ["Apples","Bananas","Cherries"]
tup1 = (13,12,15)

# items is what you want your items to be know as
# as you iterate through them in the list

# go over every item in the list
# and print it out
# for example the for loop assigns apples as the first
# item in the list to items and then prints it out
for items in list1:
    print(items)

# iterate over each item in a data structure
# using the for loop
for items in tup1:
    print(items)

# the range function
for i in range(1,11): # always goes to one less
    print(i)

for i in range(0,11,2): # print out even numbers
    print(i)

# print out the first 10 multiples of 5
for i in range (0,51,5):
    print(i)

# you can also next for loops like this
for i in range(0,5):
    for j in range (0,3):
        print(i*j)

# end of code
