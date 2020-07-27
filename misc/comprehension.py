def makeListOfLetters(word="foobar"):
  return [letter for letter in word]

#print(makeListOfLetters())

def evenGenerator(low=0,high=25):
  return [i for i in range(low,high) if i%2==0]

print(evenGenerator())

