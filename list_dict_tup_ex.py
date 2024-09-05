# list, dictionaries and tuples exercises

# 1. Create a list of names and print the second item. 
name = ["Jack","Jill","Brad","Timmy"]
print(name[1])

# 2. Create a list of sports and then replace the second
# item with another sport.
sports = ["Tennis","Baseball","Soccer","AFL"]
sports[1] = "Cricket"
print(sports)

# 3. Create an list containing numbers and delete the fifth 
# number from the array.  
numbers = [1,2,3,4,5,6,7,8,9,10]
del(numbers[4])
print(numbers)

# 4. Create two list of numbers and merge them.  
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
num3 = num1 + num2
print(num3)

# 5. Create an list of numbers and find the length,
# minimum, and maximum.  
num4 = [1,100,20,50,34,84,83,92]
print(len(num4)) # expected output 8
print(min(num4)) # expected output 1
print(max(num4)) # expected output 100

# 6. Create a dictionary of students and scores print
# out a student’s score.
students = {"Brad":100,"Jenny":90,"Sam":84,"Jessica":69}
print(students["Sam"]) # expected output is 84

# 7. Create a dictionary with the key being names and
# values being ages and then delete the second key/value pair.
names = {"Peter":18,"Jill":19,"Timmy":22}
del(names["Jill"])
print(names)

# 8. Create a dictionary of names and ages and then print out
# all the keys and values 
names2 = {"Jessica":22,"Kate":20,"Ruby":32,"Sky":33}
print(names2.items())

# 9. Create a tuple of your favorite movies 
movies = ("Matrix","Truman Show","Fugative","Inside Out")
print(movies)

# 10. Create a tuple and print all the items from 
# the first to third index
shows = ("TMNT","Get Smart","Breaking Bad","Full House","X Files")
print(shows[0:3])

# end of code
