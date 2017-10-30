# testmodule.py
print ('the test module has started')

print("__name__is", __name__)

if __name__== "__main__":
    print("I am the main program.")
else:
    print("Another module is importing me.")
    
