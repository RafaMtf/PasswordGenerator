import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3 = chr(random.randint(65,90))
uppercaseLetter4 = chr(random.randint(65,90))

lowercaseLetter1 = chr(random.randint(65,90))
lowercaseLetter2 = chr(random.randint(65,90))

randomDigit1 = int(random.randint(0,9))
randomDigit2 = int(random.randint(0,9))
randomDigit3 = int(random.randint(0,9))
randomDigit4 = int(random.randint(0,9))

ponctSign1 = chr(random.randint(33,47))
ponctSign2 = chr(random.randint(33,47))

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1.lower() + lowercaseLetter2.lower() +  str(randomDigit1) + str(randomDigit2) +str(randomDigit3) + str(randomDigit4) + ponctSign1 + ponctSign2
password = shuffle(password)

site = input("Informe o site que deseja criar uma senha:\n")

with open('passwd.txt', 'a') as f:
  f.write(site + ': ' + password + '\n')
