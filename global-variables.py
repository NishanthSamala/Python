# The global Keyword
def myfunc():
  global x
  x = "easy to learn"
myfunc()

print("Python is" + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)