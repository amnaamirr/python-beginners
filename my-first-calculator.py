a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = input("choose an operator to perform calculation: ")

if c == "+" :
  print (a+b)
elif c == "-" :
  print (a-b)
elif c == "*" :
  print (a*b)
elif c == "/" :
  print (a/b) 
else :
  print (" this operation cannot be performed")  
    