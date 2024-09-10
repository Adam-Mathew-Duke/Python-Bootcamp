# OS functions plus File input and output

# a build in Python module
import os

# a function to get the current working directory Cwd()
# do if we create a file it will be saved in the
# current working directory by Python
print(os.getcwd())

# change the current working directory for Python
# on Windows OS it's a double backslash \\
# on Mac OSs it's one forward slash /
os.chdir('C:\\Users\\0soyf\\OneDrive\\Desktop')

# the current working cwd directory has changed
print(os.getcwd())

# change back to the default cwd()
os.chdir('PYTHON')

# print out the cwd()
print(os.getcwd())

# create a text file
# python_text.txt

# list the contents of the current working directory cwd()
print(os.listdir('.'))

# open the text file that we created
myFile = open('python_text.txt')

# read the file we just opened
print(myFile.read())

# close the file
myFile.close()

# open our text file again
myFile = open('python_text.txt')

# open with each file stored as a new line
# seperated by a comma , read as comma seperated values
print(myFile.readlines())

# close our file because we have finished reading it
# and now we want to write to it
myFile.close()

# open our file for writing this time
# add a w argument for write
# add w+ for write and read
myFile = open('python_text.txt','w')

# write the text our file
# the write function will overwrite the 
# previous contents of the text file
# so there is only the text Hello World!
# in the file now
myFile.write('Hello world!\n')
myFile.close()

# a stand for append to the file
# appends the content to the next line
myFile = open('python_text.txt','a')
myFile.write('This is the second line of text\n')
myFile.close()

# end of code
