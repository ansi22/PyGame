#global variables

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

game_on=True
winner = None
current_player = "X"

#function to display the setup

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#function to choose the position for marking for each player

def whose_turn(player):
  print(player+"'s turn")
  position=input("CHOOSE POSITION B/W 1-9 ")
  temp=False
  while not temp:
      while position not in ["1","2","3","4","5","6","7","8","9"]:
         position=input("OOPS..ENTER A VALID INPUT B/W(1-9): ")
      position=int(position)-1
      if board[position]=="-":
        temp=True
      else:
         print("OOPS..POSITION ALREADY TAKEN..TRY AGAIN")
  board[position]=player
  display_board()

#function for checking if winning condition lies in row 

def row_check():
  global game_on
  row_1= board[0]==board[1]==board[2]!="-"
  row_2= board[3]==board[4]==board[5]!="-"
  row_3= board[6]==board[7]==board[8]!="-"

  if row_1 or row_2 or row_3:
    game_on= False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

#function for checking if winning condition lies in column

def column_check():
  global game_on
  column_1= board[0]==board[3]==board[6]!="-"
  column_2= board[1]==board[4]==board[7]!="-"
  column_3= board[2]==board[5]==board[8]!="-"

  if column_1 or column_2 or column_3:
    game_on= False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

#function for checking if winning condition lies in diagonal

def diagonal_check():
  global game_on
  diagonal_1= board[0]==board[4]==board[8]!="-"
  diagonal_2= board[2]==board[4]==board[6]!="-"
  
  if diagonal_1 or diagonal_2:
    game_on= False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return


#function to check for winner

def win_check():
 global winner
 row_winner=row_check()
 column_winner=column_check()
 diagonal_winner=diagonal_check()

 if row_winner:
   winner=row_winner
 elif column_winner:
   winner=column_winner
 elif diagonal_winner:
   winner=diagonal_winner
 else:
  winner=None  
 return

#function to draw the board

def draw_check():
  global game_on
  if "-" not in board:
    game_on=False
  return

#fuction to flip the player

def next_player():
  global current_player
  if current_player=="X":
   current_player="O"
  elif current_player=="O":
   current_player="X"
  return

#function for game over check

def game_over_check():
  win_check()
  draw_check()

#function to play game

def play_game():
  display_board()
  while game_on:
    whose_turn(current_player)
    game_over_check()
    next_player()
  if winner=="X" or winner=="O":
    print(winner+" won.")
  elif winner==None:
    print("Tie.")

#function to check if user wants to replay

def replay():
    play_again = input("WANNA PLAY AGAIN..(y/n) ? ")
    while play_again not in ["y","n"]:
      play_again= input("OOPS..ENTER A VALID INPUT EITHER y OR n: ")
    if play_again.lower() == 'y':
        return True
    if play_again.lower() == 'n':
        return False

#function to update the board

def update_board():
  global board
  global game_on
  global winner
  global current_player
  board=["-","-","-",
       "-","-","-",
       "-","-","-"]
  game_on=True
  winner = None
  current_player = "X"

#main
if __name__ == "__main__":
      print("****************************************************")
      print("\t\t\t\t\tTIC-TAC-TOE")
      print("****************************************************")

      while True:
        play_game()
        if not replay():
         break
        update_board()
