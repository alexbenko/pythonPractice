#Helper Functions
def displayBoard(one,two,three):
  print('\n')
  print('-----------Tic-Tac-Toe------------')
  print('\n')
  print(one)
  print(two)
  print(three)
  print('\n')
  print('-----------Tic-Tac-Toe------------')
  print('\n')

def isEven(moves):
  return moves % 2 == 0

def validMove(row,column):
  if row[column - 1] == '':
    return True
  else:
    return False

#todo: figure out a better way to do this so i dont repeat a lot of code
def getRow(currentPiece,player1,player2):
  while True:
    try:
      if currentPiece == 'X':
        whichRow = int(input(f'{player1} which row would you like to play your piece? [1,2,3]: '))
      else:
        whichRow = int(input(f'{player2} which row would you like to play your piece? [1,2,3]: '))
    except ValueError:
      print('Invalid Input, Please Only type the numbers 1,2,3 Please Try Again')
      continue
    if whichRow == 1 or whichRow == 2 or whichRow == 3:
      return whichRow
    else:
      print('Invalid input, only enter 1,2, or 3')
      continue

def getCol():
  while True:
    try:
      column = int(input('Which column would you like to place your piece [1,2,3]: '))
    except ValueError:
      print('Invalid Input, Please Try Again')
      continue
    if column == 1 or column == 2 or column == 3:
      return column
    else:
      print('Invalid input, only enter 1,2, or 3')
      continue

def checkRow(row,piece):
  #creates a new array with the given piece if it exists in given row
  #if there is a length 3, that piece wins
  #returns true if that piece wins, otherwise it will return false
  return (len([i for i in row if i == piece]) == 3)

def checkCols(one,two,three,piece):
  if one[0] == piece and two[0] == piece and three[0] == piece:
    return True
  elif one[1] == piece and two[1] == piece and three[1] == piece:
    return True
  elif one[2] == piece and two[2] == piece and three[2] == piece:
    return True
  else:
    return False

def checkDiags(one,two,three,piece):
  if one[0] == piece and two[1] == piece and three[2] == piece:
    return True
  elif one[2] == piece and two[1] == piece and three[0] == piece:
    return True
  return False


def checkForWinner(one,two,three):
  if checkRow(one,'X') or checkRow(two,'X') or checkRow(three,'X'):
    return 'X'
  elif checkRow(one,'O') or checkRow(two,'O') or checkRow(three,'X'):
    return 'O'
  elif checkCols(one,two,three,'X'):
    return 'X'
  elif checkCols(one,two,three,'O'):
    return 'O'
  elif checkDiags(one,two,three,'X'):
    return 'X'
  elif checkDiags(one,two,three,'O'):
    return 'O'
  else:
    return False



#actual game function
def ticTac():
  while True:
    try:
      toPlay = input("Would You Like To Play Tic Tac Toe? [y/n]: ")
    except ValueError:
      print('Invalid Input, Please Try Again')
      continue
    if toPlay == 'y' or toPlay == 'n':
      break
    else:
      print('Not y or n, please only enter these values')
      continue

  if(toPlay == 'n'):
    print('Goodbye :(')
    quit()

  player1 = input('Enter name of Player 1: ')
  player2 = input('Enter name of Player 2: ')
  print(f'Welcome {player1} and {player2}. {player1} is X and {player2} is O. {player1} goes first')

  currentPiece = ''
  row1 = ['','','']
  row2 = ['','','']
  row3 = ['','','']
  moves = 0

  #only 9 possible total moves
  while moves <= 9:
    displayBoard(row1,row2,row3)
    if(isEven(moves)):
      currentPiece = 'X'
    else:
      currentPiece = 'O'

    while True:
      row = getRow(currentPiece,player1,player2)
      col = getCol()

      if row == 1:
        if validMove(row1,col):
          row1[col - 1] = currentPiece
          break
        else:
          print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
          continue
      elif row == 2:
        if validMove(row2,col):
          row2[col - 1] = currentPiece
          break
        else:
          print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
          continue
      else:
        if validMove(row3,col):
          row3[col - 1] = currentPiece
          break
        else:
          print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
          continue

    moves += 1

    if moves >=3:
      print(f'{moves}total moves detected, checking for Winner...')
      if checkForWinner(row1,row2,row3) == 'X':
        print(f'{player1} is the Winner!')
        break
      elif checkForWinner(row1,row2,row3) == 'O':
        print(f'{player2} is the Winner!')
        break

    print('No Winner Yet. Continue Playing :)')


  print('Tie Game !')







ticTac()