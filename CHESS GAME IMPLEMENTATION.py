# Define the chessboard
chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

# Function to print the chessboard
def print_chessboard(chessboard):
    for row in chessboard:
        print(' '.join(row))

# Function to check if a move is valid
def is_valid_move(chessboard, start, end):
    # Check if the start and end positions are within the chessboard
    if start[0] < 0 or start[0] > 7 or start[1] < 0 or start[1] > 7 or end[0] < 0 or end[0] > 7 or end[1] < 0 or end[1] > 7:
        return False
    
    # Check if the start position is not empty
    if chessboard[start[0]][start[1]] == ' ':
        return False
    
    # Check if the end position is empty or contains an opponent's piece
    if chessboard[end[0]][end[1]] != ' ' and chessboard[end[0]][end[1]].islower() == chessboard[start[0]][start[1]].islower():
        return False
    
    # Check if the move is valid for the piece
    piece = chessboard[start[0]][start[1]]
    if piece == 'P':
        if start[0] == 1 and end[0] == 3 and chessboard[2][start[1]] == ' ' and chessboard[3][start[1]] == ' ':
            return True
        elif end[0] == start[0] + 1 and chessboard[end[0]][end[1]] == ' ':
            return True
        elif end[0] == start[0] + 1 and abs(end[1] - start[1]) == 1 and chessboard[end[0]][end[1]].islower():
            return True
        else:
            return False
    elif piece == 'p':
        if start[0] == 6 and end[0] == 4 and chessboard[5][start[1]] == ' ' and chessboard[4][start[1]] == ' ':
            return True
        elif end[0] == start[0] - 1 and chessboard[end[0]][end[1]] == ' ':
            return True
        elif end[0] == start[0] - 1 and abs(end[1] - start[1]) == 1 and chessboard[end[0]][end[1]].isupper():
            return True
        else:
            return False
    elif piece == 'R' or piece == 'r':
        if start[0] == end[0] or start[1] == end[1]:
            return True
        else:
            return False
    elif piece == 'N' or piece == 'n':
        if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
            return True
        elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
            return True
        else:
            return False
    elif piece == 'B' or piece == 'b':
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        else:
            return False
    elif piece == 'Q' or piece == 'q':
        if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        else:
            return False
    elif piece == 'K' or piece == 'k':
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True
        else:
            return False
    else:
        return False

# Function to make a move
def make_move(chessboard, start, end):
    if is_valid_move(chessboard, start, end):
        chessboard[end[0]][end[1]] = chessboard[start[0]][start[1]]
        chessboard[start[0]][start[1]] = ' '
        return True
    else:
        return False

# Main game loop
def play_chess():
    player = 1
    while True:
        print_chessboard(chessboard)
        if player == 1:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        start = input("Enter the start position (e.g., a2): ")
        end = input("Enter the end position (e.g., a4): ")
        start = (int(start[1]) - 1, ord(start[0]) - ord('a'))
        end = (int(end[1]) - 1, ord(end[0]) - ord('a'))
        if make_move(chessboard, start, end):
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print("Invalid move. Try again.")

# Start the game
play_chess()
