from random import randint

def isMatch(toMatch=1001):
  i = 0

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
