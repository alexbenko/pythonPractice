def multiply(*args):
  output = 1
  for num in args[0]:
    output *= num

  return output

print(multiply([num for num in range(1,100)]))
