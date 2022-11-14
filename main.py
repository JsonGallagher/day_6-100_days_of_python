username = input("Username: ")
password = input("Password: ")

if username.lower() == "jason" and password == "1234":
  print("Welcome Jason!")
elif username.lower() == "Bob" and password == "1234":
  print("Welcome Bob!")
elif username.lower() == "John" and password == "1234":
  print("Welcome John!")
else:
  print("Please enter a corret username and password")