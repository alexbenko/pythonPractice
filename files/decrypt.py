def openFile():
  file = open("passwords.txt","r")

  if file.mode == "r":
    fileContents = file.readlines()
    print(fileContents)

  file.close()



def decrypt(fileName="passwords.txt"):
  with open(fileName) as file:
    #removes \n from each line of the file
   contents = [line.rstrip('\n') for line in file]

   for password in contents:
     flipped = password[::-1]
     decrypted = ""
     for char in flipped:
       if char == "Z" and flipped[flipped.find(char) + 1] == "Z":
         print("f")
         decrypted += "f"
       elif char == "A":
          decrypted += "1"




decrypt()

