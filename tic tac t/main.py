3


board = [" " for i in range(9)]


def display_board():
    print("\n")
    print(" ", board[0], "|", board[1], "|", board[2])
    print("-----------")
    print(" ", board[3], "|", board[4], "|", board[5])
    print("-----------")
    print(" ", board[6], "|", board[7], "|", board[8])
    print("\n")


def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],   
        [0,4,8], [2,4,6]             
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def check_tie():
    return " " not in board


def play_game():
    current_player = "X"
    
    while True:
        display_board()
        
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            
            if move < 0 or move > 8:
                print("Invalid position! Choose 1-9.")
                continue
            
            if board[move] != " ":
                print("Position already taken! Try again.")
                continue

            board[move] = current_player

        
            if check_win(current_player):
                display_board()
                print(f"🎉 Player {current_player} wins!")
                break

        
            if check_tie():
                display_board()
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number (1-9).")

while True:
    board = [" " for i in range(9)]
    play_game()
    
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
