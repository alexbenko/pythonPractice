quarterProfits = (-20000,-16400,22000,-30000)

def areYouMakingMoney(profits):
  total = 0
  for i in profits:
    total += i

  #if profited
  if total > 0:
    return f"You profitted ${total} this year. Congrats!"
  #if loss
  elif total < 0:
    return f"You lost ${total} this year. Time to step it up"
  #otherwise you broke even
  else:
    return "You Broke even this year"

print(areYouMakingMoney(quarterProfits))
#prints the loss statement

