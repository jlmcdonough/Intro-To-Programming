# CMPT 120 Intro to Programming
# Lab #7 - Lists and Functions
# Author: Joseph McDonough
# Created: 2018-11-08

symbol = [ " ", "x", "o" ]
mark = [" "," "," "," "," "," "," "," "," "]
def printRow(row):
    output = "|"
    for cell in row:
            output+= " " + symbol[cell] + "|"
    print(output)

def printBoard(board):
    global mark    
    border = "+-----------+"
    for i in range(0,7):
        if(i%2==0):
            print(border)
        elif(i==1):
            print("| " + str(mark[0]) + " | " + str(mark[1]) + " | " + str(mark[2]) + " |")
        elif(i==3):
            print("| " + str(mark[3]) + " | " + str(mark[4]) + " | " + str(mark[5]) + " |")
        elif(i==5):
            print("| " + str(mark[6]) + " | " + str(mark[7]) + " | " + str(mark[8]) + " |")

def markBoard(board, row, col, player):
    global mark    
    index = 0
    for i in range(1,4): #row
        for j in range(1,4):  #col    
            if(row==str(i) and col==str(j) and mark[index]==" "):  #loops takes it across the top row and then down to the next row. Index starts at 0, meaning top left, and increases with the for-loops
                if(player==1):
                    mark[index] = symbol [1]
                    return True
                else:
                    mark[index] = symbol[2]
                    return True
            index+=1
    return False


def getPlayerMove():
    userInput = input("What row and column would you like your next move to be placed at. Separate the numbers with a space.") # prompt the user separately for the row and column numbers
    row, col = userInput.split(" ",1)
    return (row, col) # then return that row and column instead of (0,0)
def hasBlanks(board):
    while hasBlanks:
        for i in mark:
            if(i==" "):
                return True
        return False
    
def main():
    board = [] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if(markBoard(board,row,col,player)==False):
            print("That spot is already taken. Pick another one")
        else:
            player = player % 2 + 1 # switch player for next turn
        
main()
