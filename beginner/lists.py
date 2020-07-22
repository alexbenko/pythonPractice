def listPrac(foo):
  for i in foo:
    print(i)

#listPrac(["Hello", 123,1.2345])

#if the item in the list is a type of number, double it
def doubleList(data=["foobar",1,24,"banana",1.23]):
  for i in range(len(data)):
    print(i)
    if isinstance(data[i],int) or isinstance(data[i],float):
      #first time debugging in python!!
      print("number")
      data[i] = data[i] * 2
    else:
      continue
  return data

#print(doubleList())


def removeString(data = ['foobar',1,24,'banana']):
  for i in data:
    if isinstance(i,str):
      print('Removing String...')
      data.remove(i)

  return data



print(removeString()
)