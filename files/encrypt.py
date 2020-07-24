def encrypt(password="foobar123"):
  flipped = password[::-1]
  encrypted = ""

  for char in flipped:
    if char == "1":
      encrypted += "A"
    elif char == "2":
      encrypted += "B"
    elif char == "3":
      encrypted += "C"
    elif char == "o":
      encrypted += "0"
    elif char == "f":
      encrypted += "ZZ"
    else:
      encrypted += char


  print(encrypted)
  return encrypted

encrypt()

def savePasswords(passwords=["foobar123"]):
  file = open("passwords.txt","w+")

  print("Saving Passwords...")
  for i in range(100):
    print(i)
    file.write(encrypt() + "\n")

  #if i had a realistic file to read
  #for i in range(len(passwords)):
    #print(i)
    #file.file.write(encrypt(passwords[i]) + "\n")

  file.close()

  print("Passwords Saved !")


savePasswords()


