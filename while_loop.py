# while loops and control statements
# will continue to run until the condition becomes false
# very useful when you don't know how many times you are
# going to iterate

c = 0 # the counter

while c < 5: # do this while true
    print(c) # print the value of the counter
    c+=1 # increment the counter

# using the break control statement
c = 0

while (c < 5):
    print(c)
    c+=1

    # terminate the while loop
    if (c == 3):
        break

# using the continue control statement
c = 0

while (c < 5):

    c+=1 # have to increment the counter first

    # skip current iteration go back to the top of the loop    
    if (c == 3):
        continue
    else:
        print(c)

c = 0

while (c < 5):
    c+=1
    if c == 3:
        # take no action
        pass
    else:
        print(c)

# end of code
