def ticTac():
  row1 = ['','','']
  row2 = ['','','']
  row3 = ['','','']
  toPlay = input("Would You Like To Play Tic Tac Toe? [y/n] ")

  if toPlay == 'y':
    print(row1)
    print(row2)
    print(row3)
    break
  elif toPlay == 'n':
    print('GoodBye :(')
    break
  else:
    print('Please type y or n and hit enter')

ticTac()