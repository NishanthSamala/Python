# AND Operators
a = "True"
b = ""
print(bool(a) and bool(a)) # if both cases are the thel it is true or else flase
print(bool(a) and bool(b)) 
print(bool(b) and bool(a)) 
print(bool(b) and bool(b))
print(not bool(b))
print(not bool(a))
#Logical and operators on non-boolean types in python
#x = 0 # Zero(0) stands for false and any other number except zero is truw
#y = 4
#a = 4
#b = 7

#print(x and y)
#(a and b)

#OR Operators
c = ""
d = "false"
print(bool(c) or bool(c)) #in OR any case is ture then it is true
print(bool(c) or bool(d))
print(bool(d) or bool(c))
print(bool(d) or bool(d))