# copying, moving and renaming files
import os
import shutil

# the current working directory
os.getcwd()

# copying files
shutil.copy('python_text.txt','../')

# moving files
shutil.move('python_text.txt','../')

# renaming files with copy
shutil.copy('python_text.txt','python_test.txt')

# renaming files with move
shutil.move('python_text.txt','python_test.txt')

# end of code
