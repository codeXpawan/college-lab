import numpy as np

def display(board):
    for row in board:
        print(row)
        
def is_safe(board, x, y, num):
    #checking for row
    if (num in board[x]):
        return False
    #checking for coloum
    for row in range(9):
        if (num == board[row][y]):
            return False
    #check for 9 cell
    for r in range((x//3)*3,((x//3)*3)+3):
        for c in range((y//3)*3,((y//3)*3)+3):
            if(board[r][c]==num):return False
    
    return True
        
        
def random_value_adder(board,value):
    for i in range(value):
        while True:
            x = np.random.randint(0,8+1)
            y = np.random.randint(0,8+1)
            if(board[x][y]==''):
                break
        while True:
            num = str(np.random.randint(1,9+1))
            if(is_safe(board, x, y, num)):
                board[x][y] = num
                break
    return board

def solve_sudoku(board, x, y):
    if(y==9):
        x+=1;y=0
    if(x==9):
        return True
    if(board[x][y]==''):
        for num in range(1,10):
            if(is_safe(board,x,y,str(num))):
                board[x][y]=str(num)
                if(solve_sudoku(board,x,y+1)):return True
                board[x][y]=''
        return False
    else:
        return solve_sudoku(board,x,y+1)


board = [[""]*9 for i in range(9)]
value = int(input('Enter the value of number you want to add randomly (max-20): '))
random_value_adder(board,value)
print("Sudoko before Solving!!")
display(board)
solve_sudoku(board,0,0)
print("Sudoko after Solving!!")
display(board)