# lists

# create a list of fruits and print it out
shopping_list = ["Apple","Orange","Banana","Cheese"]
print(shopping_list)

# print out the item at index 0 and index 3
print(shopping_list[0])
print(shopping_list[3])

# remember the range does not include the last index
print(shopping_list[0:2])
print(shopping_list[0:3])

# add a new item to the end of a list
shopping_list.append("Blueberries")
print(shopping_list)

# replace the item in the list at index 0
shopping_list[0] = "Cherries"
print(shopping_list)

# delete the item at index 1 from the list
del shopping_list[1]
print(shopping_list)
print(len(shopping_list))

# make a list of lunch items
shopping_list2 = ["bread", "jam", "peanut butter"]
print(shopping_list2)

# concatinate the two lists together into one big list
print(shopping_list + shopping_list2)
print(shopping_list*2)

# create a list of numbers
listnum = [1,4,7,23,6]

# find the biggest number within the list
print(max(listnum))

# find the smallest number within the list
print(min(listnum))

# end of code
