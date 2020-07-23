user = {
  "name": "Alex",
  "age": 16,
  "bDay": "05/21"
}

def isOfAge(data):
  if data["age"] < 18:
    return False
  else:
    return True

def allowIn():
  if isOfAge(user):
    return "Welcome"
  else:
    return "You're not 18"

#print(allowIn())
#prints Youre not 18 as expected


student = {
  "name":"Alex",
  "age": 22,
  "scores": {"test1":90,"test2":85,"test3":100,"test4":92,"test5":100}
}

def average(studentData):
  length = len(studentData["scores"])
  total = 0
  for score in studentData["scores"]:
    print(score)
    total += studentData["scores"][score]

  return total / length

print(average(student))
