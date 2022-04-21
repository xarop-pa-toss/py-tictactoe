from random import randrange
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
sign = 'X'
Game = False
running = True



def display_board(board):
    for i in range(3):
        for k in range(3):
            slot = board[i][k]
            print(
                f'''
                +---------+
                |         |
                |    {slot}    |
                |         |
                +---------+
                '''
                )
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    
    while True:
        try:
            choice = int(input("Where do you want to place your 'O'? "))
        except ValueError:
            print("Sorry, couldn't understand that.. Can you try again please?")
            continue
        else:
            for i in range(3):
                for k in range(3):
                    if board[i][k] == choice:
                        board[i][k] = sign
                        break
                    else: continue
            break
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

def make_list_of_free_fields(board):
    
    board_free = board
    
    for i in range(3):
        for k in range(3):
            value = board[i][k]
            if value is int: board_free[i][k] = 'free'
            else: board_free[i][k] = value
            
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victory_for(board):
    
    #Horizontal winning condition   
    if(board[0][0] == board[0][1] and board[0][1] == board[0][2]):    
        Game = True    
    elif(board[1][0] == board[1][1] and board[1][1] == board[1][2]):    
        Game = True    
    elif(board[2][0] == board[2][1] and board[2][2] == board[2][2]):    
        Game = True    
    #Vertical Winning Condition    
    elif(board[0][0] == board[1][0] and board[0][1] == board[0][2]):    
        Game = True    
    elif(board[1][0] == board[1][1] and board[1][1] == board[1][2]):    
        Game = True    
    elif(board[2][0] == board[2][1] and board[2][1] == board[2][2]):    
        Game = True    
    #Diagonal Winning Condition    
    elif(board[0][0] == board[1][1] and board[1][1]  == board[2][2]):    
        Game = True    
    elif(board[0][2]  == board[1][1]  and board[1][1]  == board[2][0] ):    
        Game = True    
    else:            
        Game=False

    if Game: return True
    else: return False
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
def game_over(board, sign):
    if victory_for(board):
        print(f"{sign} is the winner. Congratulations!")
        running = False
        return True

def draw_move(board):
    
    if isinstance(board[1][1], int) == True: 
        board[1][1] = sign
        return
    
    filled_slot = False
    while not filled_slot:
        col, row = randrange(2), randrange(2)
        random_slot = board[col][row]

        if isinstance(random_slot, int) == True:
            random_slot = 'X'
            filled_slot = True
            break
        else: continue
                
    # The function draws the computer's move and updates the board.

while running:
    display_board(board)
    draw_move(board)
    if game_over(board, sign) == True: break
    sign = 'O'
    display_board(board)
    enter_move(board)
    if game_over(board, sign) == True: break
    sign = 'X'