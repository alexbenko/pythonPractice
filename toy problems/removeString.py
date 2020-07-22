def removeString(data = ['foobar',1,24,'banana']):
  for i in data:
    if isinstance(i,str):
      print('Removing String...')
      data.remove(i)

  return data

#print(removeString())