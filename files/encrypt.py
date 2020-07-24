def encrypt(password="foobar123"):
  flipped = password[::-1]
  encrypted = ""

  for char in flipped:
    if char == "1":
      print("One")
      encrypted + "A"
    elif char == "2":
      encrypted + "B"
    elif char == "3":
      encrypted + "C"
    else:
      print("Not")
      encrypted + char


  return encrypted



print(encrypt())