#me messing around with function
def add(x,y):
  return x + y

#print(add(1,2))

def countLetters(word):
  counter = {}
  for letter in word:
    print(letter)
    if letter in counter:
      counter[letter] += 1
    else:
      counter[letter] = 1

  return counter

#print(countLetters("Alexander"))



