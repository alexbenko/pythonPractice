#will return the the last half of the word

def splicerHalf(word):
  halfIndex = round(len(word)/2)
  return word[halfIndex:len(word)]

print(splicerHalf("Foobar"))
# prints "bar"