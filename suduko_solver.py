# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

# def print_board():
#     boardString = ""
#     for i in range(9):
#         for j in range(9):
#             boardString += str(board[i][j]) + " "
#             if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
#                 boardString += "| "

#             if j == 8:
#                 boardString += "\n"

#             if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
#                 boardString += "- - - - - - - - - - - \n"
#     print(boardString)

import random

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def printBoard():

    for i in board:
        for j in i:
            print(j,end=' ')
        print()

def possible(x,y,n):
    #Row check
    for i in range (0,9):
        if board[x][i]==n:
            return False
    #column check    
    for j in range (0,9):
        if board[j][y]==n:
            return False
    #Block check    
    for i in range(0,3):
        for j in range(0,3):
            if board[((x//3)*3)+i][((y//3)*3)+j]==n:
                return False            
    return True

def generate_board():
    for i in range(25):
        row=random.randint(0,8)
        col=random.randint(0,8)
        num=random.randint(1,9)
        if possible(row,col,num):
            board[row][col]=num
    printBoard()
            
def solve():

    for i in range(9):          #Finds
        for j in range(9):      #Empty
            if board[i][j]==0:  #Cell

                for n in range(1,10):   #Try every number
                    if possible(i,j,n): #Possible
                        board[i][j] =n  #Places number
                        solve()         #Goes to the next cell(recursion)
                        board[i][j] =0  #So if solve fals 
                                        #in next iteration 
                                        #it checks the cell again 
                                        #with another number
                return
    printBoard()
    exit()
    return


printBoard()
print("\n\n")
generate_board()
print("\n\n")
solve()


