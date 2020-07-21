#PRacticing wiht string formating, rounding , and string literals
def poemFormat():
  return "The {1} {0} {2}".format("less","road","traveled")

#print(poemFormat())
#=> The road less traveled
#similar to string literals in javascript

def welcomeToSite(user):
  #mock site greeting
  #in real app this would pull from database
  user += 1
  return 'You have visited {v} time(s)'.format(v=user)

#print(welcomeToSite(0))

#rounds to the third decimal point
def rounded(amt = .89123):
  return 'Your final score is {s:1.3f}'.format(s=amt)

print(rounded())

def stringLiteral(string="Alex"):
  return f"Welcome {string}"

print(stringLiteral())