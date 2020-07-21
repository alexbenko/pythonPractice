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

def biggest(bucket):
  print(bucket[0])
  big = bucket[0]

  for i in bucket:
    if bucket[i] >= big:
      big = bucket[i]

  return big

test = (1,2,3)

print(biggest(test))









