a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = input("select the operator: ")

if c == "+" :
 print(a,"+",b,"=",a+b)
elif c == "-" :
  print(a,"-",b,"=",a-b) 
elif c == "*" :
  print(a,"*",b,"=",a*b)
elif c == "/" :
  print(a,"/",b,"=",a/b)
elif c == "**" :
  print(a,"**",b,"=",a**b)
else :
  print("SORRY,this operaton cannot be perfromed! ")   

