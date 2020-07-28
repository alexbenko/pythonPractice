def foobar(i):
  if i % 3 == 0 and i % 5 ==0:
    return "Fizzbuzz"
  elif i == 100 :
    return "foo"
  elif i % 5 == 0:
    return "buzz"
  elif i % 3 == 0:
    return "Fizz"
  else:
    return "bar"


mapped = list(map(foobar,[i for i in range(0,1000)]))
print(mapped)