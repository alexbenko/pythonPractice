#def openFile():
 # file = open("passwords.txt","r")
#
  #if file.mode == "r":
   # fileContents = file.readlines()
    #print(fileContents)
#
#file.close()
#
#if char == "Z" and flipped[flipped.find(char) + 1] == "Z":
def decrypt(password="CBArab00Z"):
  flipped = password[::-1]
  decrypted = ""

  for char in flipped:
    if char == "Z":
      decrypted += "f"
    elif char == "A":
      decrypted += "1"
    elif char == "B":
      decrypted += "2"
    elif char == "C":
      decrypted += "3"
    elif char == "0":
      decrypted += "o"
    else:
      decrypted += char

  print(decrypted)
  return decrypted



def saveDecrypted(fileName="passwords.txt"):
  #only works for the string "foobar123"
  with open(fileName) as file:
    #removes \n from each line of the file
    contents = [line.rstrip('\n') for line in file]
    newFile = open("decryptedPasswords.txt","w+")

    print("Decrypting...")
    for password in contents:
      newFile.write(decrypt(password) + "\n")

  print("Decrypted!")
  newFile.close()



saveDecrypted()




