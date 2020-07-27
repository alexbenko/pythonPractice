from random import randint

def isMatch():
  userInput = input('Enter a whole number to randomly generate to: ')

  #simple way to test for decimals
  if '.' in userInput:
    userInput = input('Please Enter a whole number to randomy generate to: ')

  toMatch = int(userInput)
  current = randint(0,toMatch)
  i = 1

  while True:
    if(current == toMatch):
      break

    print(current)
    i += 1
    current = randint(0,toMatch)

  return(f"Randomly Generated {toMatch}. Completed in {i} tries")


print(isMatch())