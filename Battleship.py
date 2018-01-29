from random import randint

__author__ = "Albert Leung"
__credits__ = "Codecademy"
#--------------------------------------------------------------
print "--------------------------------------------------------------"    
print "__________    ___________________________.____     ___________"
print "\______   \  /  _  \__    ___/\__    ___/|    |    \_   _____/"
print " |    |  _/ /  /_\  \|    |     |    |   |    |     |    __)_ "
print " |    |   \/    |    \    |     |    |   |    |___  |        \ "
print " |________/\____|____/____|     |____|   |________\/_________/ "
print "  _________ ___ ___ ._____________       "                     
print " /   _____//   |   \|   \______   \    "                       
print " \_____  \/    ^    \   ||     ___/   "                        
print " /        \    Y    /   ||    |       "                        
print "/_________/\___|_  /|___||____|        v2.0   by Albert Leung   "
print "--------------------------------------------------------------"    

print
player_name = str(raw_input('What is your name?'))
print 
print "Welcome %s!" %player_name.upper() 
print
print "Goal: sink the battleship before you run out of cannons"
print "Easy:     3 x 3 board      5  cannons"
print "Medium:   4 x 4 board      8  cannons"
print "Hard:     5 x 5 board      10 cannons"
print
#---------------------------------------------------------------
def prompt_for_difficulty():
  print "Which difficulty would you like to go with?"
  print "(E)asy / (M)edium / (H)ard"
  difficulty = raw_input().upper()
  
  global board_size 
  global total_turn
  
  if difficulty == "E" or difficulty == "EASY":
    board_size = 3
    total_turn = 5
  elif difficulty == "M" or difficulty == "MEDIUM":
    board_size = 4
    total_turn = 8
  elif difficulty == "H" or difficulty == "HARD":
    board_size = 5
    total_turn = 10
  else:
    print "Expected e, m, or h. Please try again."
    print
    prompt_for_difficulty()
#---------------------------------------------------------------
prompt_for_difficulty()
#---------------------------------------------------------------
def play_again():
  print
  print "Play again?"
  print "(Y)es / (N)o"
  keep_playing = raw_input().upper()

  if keep_playing == "Y" or keep_playing == "YES":
    prompt_for_difficulty()
    create_board()
    game_loop(board_size, total_turn,board)
  elif keep_playing  == "N" or keep_playing == "NO":
    print "Thank you for playing."
    return
  else:
    print "Expected y or n. Please try again."
    print
    play_again()
#--------------------------------------------------------------- 
def print_board(board):
  print "  ",
  for index in range(board_size):
    print "  %d       " %(index+1),
  print
  
  row_num = 1
  for row in board:
    
    print "  ",
    for x in row:
      if x == "A":
        print "  _       ",
      elif x == "O":
        print " ~~~      ",
      else:
        print "__ __     ",
    print
    
    print " %d" %row_num,
    for x in row:
      if x == "A":
        print " / \      ",
      elif x == "O":
        print "~~~~~     ",
      else:
        print "\ V /     ",
    print
    
    print "  ",
    for x in row:
      if x == "A":
        print "/ ^ \     ",
      elif x == "O":
        print "~~~~~     ",
      else:
        print " ) (      ",
    print
    
    print "  ",
    for x in row:
      if x == "A":
        print "\_W_/     ",
      elif x == "O":
        print " ~~~      ",
      else:
        print "/_n_\     ",
        
    row_num += 1
    print
    print
    print
    #print " ".join(row)
#---------------------------------------------------------------
def random_row(board):
  return randint(0, len(board) - 1)
#---------------------------------------------------------------
def random_col(board):
  return randint(0, len(board[0]) - 1)
#---------------------------------------------------------------
def create_board():
  global board
  board = []
  for x in range(board_size):
    board.append(["O"] * board_size)

  print
  print_board(board)
  print
  
  global ship_row
  global ship_col
  
  ship_row = random_row(board)
  ship_col = random_col(board)
#---------------------------------------------------------------
create_board()
#Not mine------------------------------------------------------
def input_number(message):
  while True:
    try:
       userInput = int(input(message))       
    except:
       print("Not an integer, try again.")
       continue
    else:
       return userInput 
       break 
#--------------------------------------------------------------
#print ship_row
#print ship_col
#--------------------------------------------------------------
#Game loop-----------------------------------------------------
def game_loop(game_board, game_turn, board):
  for turn in range(game_turn):
    print "Turn", turn + 1
    print "You have %d cannons left." %(game_turn-turn)

    guess_row = input_number("Guess Row: ")-1
    guess_col = input_number("Guess Col: ")-1
  
    print
#win----------------------------------------------------------- 
    if guess_row == ship_row and guess_col == ship_col:
      board[guess_row][guess_col] = "A"
      print
      print_board(board)
      print "Congratulations! You Win!"
      play_again()
      break
#wrong---------------------------------------------------------
    else:
      if (guess_row < 0 or guess_row > (game_board-1)) or (guess_col < 0 or guess_col > (game_board-1)):
        print "Oops, your cannon did not even land in the ocean."
      
      elif(board[guess_row][guess_col] == "X"):
        print "You tried that block already."
      
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      if turn == (game_turn-1):
        print_board(board)
        print "Game Over! You run out of cannons."
        print
        play_again()
        break
  # Print (turn + 1) here!
      print
      print_board(board)
      print 
      print "--------------------------------------------------------------"    
#--------------------------------------------------------------
#Main----------------------------------------------------------
game_loop(board_size,total_turn,board)


    
  