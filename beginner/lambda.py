#seeing how lambda function's work

def halver(n):
  return lambda a : a / n

myHalver = halver(2)

print(myHalver(10))

