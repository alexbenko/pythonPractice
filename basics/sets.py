def uniquer(newSet):
  return set(newSet)


foobar = [1,1,1,"foo","foo","bar","bar","bar",30,30,30]

print(uniquer(foobar))
#=> {'foo', 1, 30, 'bar'}