class TicTacToe:
  currentPiece = ''
  row1 = ['','','']
  row2 = ['','','']
  row3 = ['','','']
  moves = 0

  def __init__(this,player1,player2):
    print('Tic Tac Toe Game Initialized...')
    this.player1 = player1
    this.player2 = player2
