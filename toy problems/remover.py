#removes specified letter from given string
def remover(string, letter):
  return string.split(letter)

print(remover("Hello World", "l"))
