file = open('file_example.txt', 'r') # open in read mode
contents = file.read() # assign all text to string (with \n)
print(contents)
file.close() # ALWAYS close open files!
