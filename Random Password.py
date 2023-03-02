import random
quit = False
def rpassword():
  letters_password = "abcdefghijklmnopqrstuvwxyz"
  numbers_password = "0123456789"
  symbols_password = "!@#$%^&*"
  
  new_password = letters_password + numbers_password +   symbols_password
  
  hlong = int(input("How long do you want your password to be?"))
  length_password = hlong
  
  password = "".join(random.sample(new_password, 
  length_password))
  print("Generated Password: ", password)
while quit != True:
  user = (input("Do you want a random password?"))
  if user == 'yes':
    rpassword()
  else:
    print("See you later")
    quit = True
