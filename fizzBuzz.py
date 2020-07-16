def fizzBuzz(x):
  if x % 5 == 0 & x % 3 == 0:
    print("FizzBuzz")
  elif x % 5 == 0:
    print("Buzz")
  elif x % 3 == 0:
    print("Fizz")
  else:
    print("Foobar")

fizzBuzz(15)