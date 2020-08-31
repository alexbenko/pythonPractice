class TicTacToe:
  player1 = ''
  player2 = ''
  currentPiece = ''
  row1 = ['','','']
  row2 = ['','','']
  row3 = ['','','']
  moves = 0

  def __init__(this):
    print('Tic Tac Toe Game Initialized...')
    this.render()

  def displayBoard(this):
    print('-----------Tic-Tac-Toe------------')
    print('\n')
    print(f'1. {this.row1}')
    print(f'2. {this.row2}')
    print(f'3. {this.row3}')
    print('\n')
    print('-----------Tic-Tac-Toe------------')

  def isEven(this):
    return this.moves % 2 == 0

  def validMove(this,row,column):
    if row[column - 1] == '':
      return True
    else:
      return False

  def getRow(this):
    while True:
      try:
        if this.currentPiece == 'X':
          whichRow = int(input(f'{this.player1} which row would you like to play your piece? [1,2,3]: '))
        else:
          whichRow = int(input(f'{this.player2} which row would you like to play your piece? [1,2,3]: '))
      except ValueError:
        print('Invalid Input, Please Only type the numbers 1,2,3. Please Try Again')
        continue
      if whichRow == 1 or whichRow == 2 or whichRow == 3:
        return whichRow
      else:
        print('Invalid input, only enter 1,2, or 3')
        continue

  def getCol(this):
    while True:
      try:
        column = int(input('Which column would you like to place your piece [1,2,3]: '))
      except ValueError:
        print('Invalid Input, Please Only type the numbers 1,2,3. Please Try Again')
        continue
      if column == 1 or column == 2 or column == 3:
        return column
      else:
        print('Invalid input, only enter 1,2, or 3')
        continue

  def checkRows(this):
    rows = [this.row1,this.row2,this.row3]

    for row in rows:
      if len([i for i in row if i == this.currentPiece]) == 3:
        return True

    return False

  def checkCols(this):
    if this.row1[0] == this.currentPiece and this.row2[0] == this.currentPiece and this.row3[0] == this.currentPiece:
      return True
    elif this.row1[1] == this.currentPiece and this.row2[1] == this.currentPiece and this.row3[1] == this.currentPiece:
      return True
    elif this.row1[2] == this.currentPiece and this.row2[2] == this.currentPiece and this.row3[2] == this.currentPiece:
      return True
    else:
      return False

  def checkDiags(this):
    if this.row1[0] == this.currentPiece and this.row2[1] == this.currentPiece and this.row3[2] == this.currentPiece:
      return True
    elif this.row1[2] == this.currentPiece and this.row2[1] == this.currentPiece and this.row3[0] == this.currentPiece:
      return True
    return False

  def checkForWinner(this):
    if this.checkRows() or this.checkCols() or this.checkDiags():
      if this.currentPiece == 'X':
        print(f'{this.player1} is the Winner!')
        this.displayBoard()
      else:
        print(f'{this.player2} is the Winner!')
        this.displayBoard()
      return True
    else:
      return False

  def render(this):
    this.player1 = input('Enter name of Player 1: ')
    this.player2 = input('Enter name of Player 2: ')
    print(f'Welcome {this.player1} and {this.player2}. {this.player1} is X and {this.player2} is O. {this.player1} goes first')

    while this.moves <= 9:
      this.displayBoard()

      if this.isEven():
        this.currentPiece = 'X'
      else:
        this.currentPiece = 'O'

      while True:
        row = this.getRow()
        col = this.getCol()

        if row == 1:
          if this.validMove(this.row1,col):
            this.row1[col - 1] = this.currentPiece
            this.moves += 1
            break
          else:
            print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
            continue
        elif row == 2:
          if this.validMove(this.row2,col):
            this.row2[col - 1] = this.currentPiece
            this.moves += 1
            break
          else:
            print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
            continue
        elif row == 3:
          if this.validMove(this.row3,col):
            this.row3[col - 1] = this.currentPiece
            this.moves += 1
            break
        else:
            print(f'A piece already exists at row: {row} and column: {col}, try a different spot')
            continue



      if this.moves >= 3:
        print(f'{this.moves} total moves detected, checking for Winner...')
        if this.checkForWinner():
          break
        print('No Winner Detected,Continuing Game...')

    if this.moves >= 10:
      print('Tie Game :/')





game = TicTacToe()