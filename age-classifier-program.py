name = input("Enter your name: ")
age = int(input("Enter your age: "))

if (age <= 1):
  print("You are an infant")
elif (age >1)and(age <13):
  print("You are a kid")
elif (age >13)and(age <20):
  print("You are a teenager") 
else :     
  print("You are an adult")