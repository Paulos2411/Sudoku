board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
print('\nWe start with the following Sudoku: \n')

def solve(board):

    find = find_empty(board)
    if not find: # find is not None
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

def valid(board, number, position):

    # Kontrolle der Zeile
    for i in range(0, len(board[0])):
        if board[position[0]][i] == number and position[1] != i :
            return False

    # Kontrolle der Spalte
    for j in range(0, len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False

    #Kontrolle der Kästchen
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

def create_board(board):
    for i in range(0, len(board[0])):
        if i % 3 == 0:
            print('- - - - - - - - - - - - - - - -')
        for j in range(0, len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  

    return None
        

print(create_board(board))
solve(board)
print('\n Solution to our Sudoku: \n')
print(create_board(board))