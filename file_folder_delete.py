# Deleting files and folders
# These are very powerful features so be very careful

import os
import shutil

print(os.getcwd())

# will remove one specific file at the current path getcwd()
# file will be delted and not recoverable in trash
os.unlink('test.txt')

# allows you to delete an empty folder
# you cannot delete a popuated folder using os.rmdir()
os.rmdir('EmptyFolder')

# allows you to delete a populated folder
# delete the folder and everything inside of that folder
# without the argument the files will be deleted but not the folder
shutil.rmtree('TEST',ignore_errors=True)

# end of code
