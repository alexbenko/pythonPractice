def fizzBuzz(x):
  if x % 5 == 0 and x % 3 == 0:
    print("FizzBuzz")
  elif x % 5 == 0:
    print("Buzz")
  elif x % 3 == 0:
    print("Fizz")
  else:
    print("Foobar")

fizzBuzz(3)
#=>"Fizz"