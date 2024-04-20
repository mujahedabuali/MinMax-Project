import random

# Define the board
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Define the symbols
EMPTY = 0
X = 1
O = -1
symbols = {X: "X", O: "O", EMPTY: " "}

# Define the human and the computer players
human = O
computer = X

# Define the winning combinations
wins = [
    [0, 1, 2], # first row
    [3, 4, 5], # second row
    [6, 7, 8], # third row
    [0, 3, 6], # first column
    [1, 4, 7], # second column
    [2, 5, 8], # third column
    [0, 4, 8], # first diagonal
    [2, 4, 6]  # second diagonal
]

# Define a function that checks if the game is over and returns the winner or None
def is_game_over(board):
    # Check for a win
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != EMPTY:
            return board[w[0]] # return X or O
    # Check for a tie
    if EMPTY not in board:
        return EMPTY # return 0
    # Otherwise, the game is not over
    return None # return None

# Define a function that evaluates the board and returns a score
def evaluate(board):
    # Check if the game is over
    result = is_game_over(board)
    # If the computer wins, return 10
    if result == computer:
        return 10
    # If the human wins, return -10
    elif result == human:
        return -10
    # If it is a tie, return 0
    else:
        return 0

# Define a function that generates a list of all the available moves on the board
def get_moves(board):
    # Initialize an empty list
    moves = []
    # Loop through the board
    for i in range(9):
        # If the square is empty, add it to the list
        if board[i] == EMPTY:
            moves.append(i)
    # Return the list
    return moves

# Define a function that implements the minimax algorithm and returns the best move and the best score for the current player
def minimax(board, player, depth):
    # Check if the game is over or the depth limit is reached
    if is_game_over(board) or depth == 0:
        # Return the score and None as the move
        return evaluate(board), None
    # Initialize the best score and the best move
    if player == computer:
        # For the computer, the best score is the lowest possible
        best_score = -float("inf")
    else:
        # For the human, the best score is the highest possible
        best_score = float("inf")
    best_move = None
    # Loop through all the possible moves
    for move in get_moves(board):
        # Make a copy of the board and apply the move
        board_copy = board.copy()
        board_copy[move] = player
        # Call the minimax function recursively with the opposite player and the reduced depth
        score, _ = minimax(board_copy, -player, depth - 1)
        # Update the best score and the best move
        if player == computer:
            # For the computer, choose the maximum score
            if score > best_score:
                best_score = score
                best_move = move
        else:
            # For the human, choose the minimum score
            if score < best_score:
                best_score = score
                best_move = move
    # Return the best score and the best move
    return best_score, best_move

# Define a function that makes a move on the board and returns the updated board
def make_move(board, move, player):
    # Make a copy of the board
    board_copy = board.copy()
    # Assign the player symbol to the move position
    board_copy[move] = player
    # Return the updated board
    return board_copy

# Define a function that prints the board in a human-readable format
def print_board(board):
    # Loop through the board
    for i in range(9):
        # Print the symbol of the square
        print(symbols[board[i]], end=" ")
        # Print a line break after every three squares
        if (i + 1) % 3 == 0:
            print()
    # Print a separator
    print("-" * 9)

# Define a function that gets the human input and validates it
def get_human_move(board):
    # Initialize a valid flag
    valid = False
    # Loop until a valid input is entered
    while not valid:
        # Prompt the human to enter a move
        move = input("Enter your move (1-9): ")
        # Try to convert the input to an integer
        try:
            move = int(move) - 1 # subtract 1 to get the board index
            # Check if the move is within the range and the square is empty
            if 0 <= move <= 8 and board[move] == EMPTY:
                # Set the valid flag to True
                valid = True
            else:
                # Print an error message
                print("Invalid move. Try again.")
        except:
            # Print an error message
            print("Invalid input. Try again.")
    # Return the move
    return move

# Define a function that runs the main loop of the game
def play():
    # Initialize the board
    board = [EMPTY] * 9
    # Initialize the game over flag
    game_over = False
    # Initialize the current player
    player = X
    # Loop until the game is over
    while not game_over:
        # Print the board
        print_board(board)
        # Check if the game is over
        result = is_game_over(board)
        if result is not None:
            # Print the result
            if result == X:
                print("X wins!")
            elif result == O:
                print("O wins!")
            else:
                print("It's a tie!")
            # Set the game over flag to True
            game_over = True
        else:
            # Check if the current player is the human or the computer
            if player == human:
                # Get the human move
                move = get_human_move(board)
            else:
                # Get the computer move using the minimax algorithm with a depth of 9
                _, move = minimax(board, computer, 9)
                # Print the potential result for each button
                print("If I move to this button, the game will end as:")
                for i in range(9):
                    if board[i] == EMPTY:
                        # Make a copy of the board and simulate the move
                        board_copy = board.copy()
                        board_copy[i] = computer
                        # Evaluate the score for the move
                        score = evaluate(board_copy)
                        # Print the result for the move
                        print(f"Button {i + 1}: {score_to_result(score)}")
                # Print the chosen move and the score
                print(f"I choose button {move + 1}, because it has the best score of {score_to_result(score)}")
            # Make the move on the board
            board = make_move(board, move, player)
            # Switch the player
            player = -player

# Define a helper function that converts the score to a result
def score_to_result(score):
    # If the score is positive, the result is win
    if score > 0:
        return "win"
    # If the score is zero, the result is draw
    elif score == 0:
        return "draw"
    # If the score is negative, the result is lose
    else:
        return "lose"

# Start the game
play()





# Define a function that prints the potential result for each button
def print_potential_result(board, player):
    # Loop through all the possible moves
    for i in range(9):
        if board[i] == EMPTY:
            # Make a copy of the board and simulate the move
            board_copy = board.copy()
            board_copy[i] = player
            # Evaluate the score for the move
            score = evaluate(board_copy)
            # Print the result for the move
            print(f"Button {i + 1}: {score_to_result(score)}")

# Modify the comp_move function to print the potential result before making a move
def comp_move(self,board): 


    if self.compFlag==False  :
        
        firsMove,icon =self.firstMove(board)

        if firsMove == True:
            ran_zero = [(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value == 0]
            ran = random.choice(ran_zero)
            bttn = self.buttons[ran[0]][ran[1]]
            indx = self.indexesBttn.get(ran, None)
        
            x =  bttn.winfo_x()
            y = bttn.winfo_y()
        
            self.press(indx+1,x,y)

        else:    
            # Print the potential result for each button
            print("If I move to this button, the game will end as:")
            print_potential_result(board, icon)
            # Choose the best move using the minimax function
            if self.player1.icon=="X":
                score, move = self.minimax_Algo(board,1,True)
            else :  
                score, move = self.minimax_Algo(board,-1,True)  

            x1,y1=move
            indx = self.indexesBttn.get(move, None)
            bttn = self.buttons[x1][y1]
            x =  bttn.winfo_x()
            y = bttn.winfo_y()
            
            # Print the chosen move and the score
            print(f"I choose button {indx + 1}, because it has the best score of {score_to_result(score)}")

            self.press(indx+1,x,y)
