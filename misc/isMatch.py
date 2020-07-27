from random import randint

def isMatch():
  userInput = input('Enter a whole number to randomy generate to:')
  if('.' in userInput):
    userInput = input('Please Enter a whole number to randomy generate to:')

  toMatch = int(userInput)
  i = 1

  current = randint(0,toMatch)
  match = current == toMatch

  while not match:
    if(current == toMatch):
      break

    print(current)
    i += 1
    current = randint(0,toMatch)

  return(f"Randomly Generated {toMatch}. Completed in {i} tries")

print(isMatch())
