import math
gameBoard = [[" " for _ in range(3)] for _ in range(3)]
rows, cols = 3, 3
def printGameBoard():
    for x in range(rows):
        print("|", end="")
        for y in range(cols):
            print(f" {gameBoard[x][y]} ", end="|")
        if x < rows - 1: 
            print("\n" + "-" * 13)
    print()
def checkForWinner():
    for row in gameBoard:  
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3): 
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] and gameBoard[0][col] != " ":
            return gameBoard[0][col]
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] != " ":
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] != " ":
        return gameBoard[0][2]
    if all(cell != " " for row in gameBoard for cell in row):
        return "Draw"
    return None
def minimax(is_maximizing):
    winner = checkForWinner()
    if winner == "X":
        return -1
    if winner == "O":
        return 1
    if winner == "Draw":
        return 0
    best_score = -math.inf if is_maximizing else math.inf
    for x in range(3):
        for y in range(3):
            if gameBoard[x][y] == " ": 
                gameBoard[x][y] = "O" if is_maximizing else "X"
                score = minimax(not is_maximizing)
                gameBoard[x][y] = " " 
                best_score = max(best_score, score) if is_maximizing else min(best_score, score)
    return best_score
def bestMove():
    best_score = -math.inf
    move = None
    for x in range(3):
        for y in range(3):
            if gameBoard[x][y] == " ":  
                gameBoard[x][y] = "O"
                score = minimax(False)
                gameBoard[x][y] = " " 
                if score > best_score:
                    best_score = score
                    move = (x, y)
    return move
turnCounter = 0
while True:
    printGameBoard()
    winner = checkForWinner()
    if winner:
        if winner == "Draw":
            print("\nIt's a draw!")
        else:
            print(f"\n{winner} has won!")
        break
    if turnCounter % 2 == 0: 
        while True:
            try:
                row_col = input("\nEnter row and column (e.g., 1 2): ")
                row, col = map(int, row_col.split())
                row, col = row - 1, col - 1  # Convert to 0-indexed
                if 0 <= row < 3 and 0 <= col < 3 and gameBoard[row][col] == " ":
                    gameBoard[row][col] = "X"
                    break
                else:
                    print("Invalid move. Cell already taken or out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
    else: 
        print("\nAI is thinking...")
        aiMove = bestMove()
        if aiMove:
            gameBoard[aiMove[0]][aiMove[1]] = "O"
            print(f"AI chooses row {aiMove[0] + 1}, column {aiMove[1] + 1}")
    turnCounter += 1
