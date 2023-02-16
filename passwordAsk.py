import bcrypt
import random

password = b'teste'
salt = bcrypt.gensalt()

hashed = bcrypt.hashpw(password, salt)

print(hashed)

'''senha = (input('digite sua senha:\n'))

if senha == password:
    with open('passwd.txt' , 'r') as f:
        print(f.read())    
else:
    print('Sorry, but your password is incorrect. \n')'''