# hello() without user input 

def hello():
    return "Hello, World!"
print(hello())

############################################################################################################################################

# hello() with user input

def hello():
    x=input("Enter user name: ")
    return f"Hello, {x}"
print(hello())
