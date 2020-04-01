username_set1 = "amnaamirr"
password_set1 = "abc123"
username_set2 = "laibaamirr"
password_set2 = "def345"

username = input("username: ")
password = input("password: ")

if (username == username_set1)and(password == password_set1): 
  print("you have logged in successfully")  
elif (username == username_set2)and(password == password_set2):
  print("you have logged in successfully")  
else :
  print("you have entered incorrect username or password")