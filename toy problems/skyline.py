#return a string whever every even letter is uppercase Foobar => fOoBaR
def skyline(word):
  output = ""
  for i in range(len(word)):
    even = i % 2 == 0
    print(not even)

    if not even:
      output += word[i].upper()

    else:
      output += word[i].lower()

  return output






print(skyline("anthropomorphism"))
#=>aNtHrOpOmOrPhIsM