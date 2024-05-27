username = input("what is your username: ")
password = input("what is your password: ")

if username == "admin" and password == "1234":
  print("You are logged in as admin")
elif username == "norah" and password != "1235":
  print("You are logged in as Norah")
elif username == "nereah" and password == "1236":
  print("You are logged in as Nereah")
else:
  print("You are not logged in")