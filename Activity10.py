from getpass import getpass

username = 'Unkn0wnM3me' 
password = 'niger'

u = input("Enter your Username --> ")
p = getpass("Enter your Password --> ")

if (u == username) and (p == password) :
	print("Login Successful")
else:
	print("Login Unsuccessful")
