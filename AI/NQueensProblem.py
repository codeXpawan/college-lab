def display(board):
    for row in board:
        print(row)
        


def is_safe(board,x, y, n):
    #column test
    for row in range(x):
        if(board[row][y] == 'Q'):
            return False
    #top-left diagonal test
    row = x-1
    col = y-1
    while row >= 0 and col >=0:
        if(board[row][col] == 'Q'):
            return False
        row -= 1
        col -= 1
    #top-right diagnoal test
    row = x-1
    col = y+1
    while row >= 0 and col <n:
        if(board[row][col] == 'Q'):
            return False
        row -= 1
        col += 1
    return True
    
def n_queens_solver(board,x,n):
    #if nQueens are place return
    if(x>=n):
        return True
    #iterate through cols for each row
    for col in range(n):
        #if the pos is safe then place queen
        if(is_safe(board,x,col,n)):
            board[x][col] = 'Q'
            #if the next queen can be placed return True
            if(n_queens_solver(board,x+1,n)):
                return True
            board[x][col] = ''
    return False

no_of_queens = int(input("Enter the n: "))
board = [[""]*no_of_queens for i in range(no_of_queens)]
# board[0][0] = 'Q'
if(n_queens_solver(board,0,no_of_queens)):
    display(board)
else:
    print('No solution')

# print(is_safe(board,1,2,no_of_queens))