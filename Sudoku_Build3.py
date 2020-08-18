#Created by @sarthak1905
#Author Name-Sarthak Saxena
#Dated 4th May,2020
#Contact me on GitHub if you find any glitches or have any recommendations!

import numpy as np
import random

#Prints the ndarray in format so it is readable(a bit at least)

def Print_Board(board):
    for i in range(9):
        for j in range(9):
            if j==0:
                print("|",end='')
            if j!=8:
                print(board[i,j],end=' ')
            else:
                print(board[i,j],end='')
            if (j+1)%3==0:
                print("|",end='')
        if (i+1)%3==0:
            print("\n---------------------",end='')
        print()

#This function finds...well...an empty cell

def Find_Empty_Cell(board):
    for i in range(9):
        for j in range(9):
            if board[i,j]==0:
                row=i
                col=j
                Fill_Chk=1
                res=np.array([row,col,Fill_Chk],dtype="int8")
                return res
    res=np.array([-1,-1,0])
    return res

#This function checks the validity of a number at a given position in the puzzle 
#Done according to sudoku rules

def Check_Validity(board,row,col,num):
    row_start=(row//3)*3
    col_start=(col//3)*3
    if num in board[:,col] or num in board[row,:]:
        return False
    if num in board[row_start:row_start+3,col_start:col_start+3]:
        return False
    return True

#Generates an unsolved sudoku board based on required difficulty
#The algorithm for difficulty generation is a little primitive, but really helpful for accuracy 

def Generate_Unsolved_Puzzle(board,difficulty):
    count,done=0,False
    if difficulty is "Easy":
        print("Easy Difficulty Puzzle Generating...\n\n")
        upper_limit=35
    elif difficulty is "Medium":
        print("Medium Difficulty Puzzle Generating...\n\n")
        upper_limit=41
    else:
        print("Hard Difficulty Puzzle Generating...\n\n")
        upper_limit=47
    while True:   
        i=random.randint(0,8)
        j=random.randint(0,8)
        if count<=upper_limit:
            if board[i,j]!=0:
                not_check=board[i,j]
                board[i,j]=0
                board_copy=board
                if Solve_Sudoku(board_copy,not_check):
                    board[i,j]=not_check
                    continue
                row_start=(i//3)*3
                col_start=(j//3)*3
                if difficulty is "Easy":
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<5:
                        board[i,j]=not_check
                        continue
                elif difficulty is "Medium":
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<4:
                        board[i,j]=not_check
                        continue
                else:
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<3:
                        board[i,j]=not_check
                        continue
                count+=1
        else:
            done=True
            break

#Input of the row, column and nummber to check is done here, so essentially playing the game lol

def Play_Sudoku(Solved_Board,Unsolved_Board):
    while True:    
        row=int(input("Enter the row to insert number:")) - 1
        col=int(input("Enter the column to insert number:")) - 1
        number_check=int(input("Enter the number(or press 10 to exit):"))
        if number_check!=10:
            if Unsolved_Board[row,col]==0:
                print(Solved_Board[row,col])
                if Solved_Board[row,col]==number_check:
                    print("Correct! Updated board:")
                    Unsolved_Board[row,col]=number_check
                    Print_Board(Unsolved_Board)
                else:
                    print("Incorrect!Updated board:")
                    Print_Board(Unsolved_Board)
            else:
                print("That location is already correctly filled!")
            if np.array_equal(Solved_Board,Unsolved_board):
                print("Congrats on solving the sudoku!")
                break
        else:
            Print_Board(Solved_Board)
            return

#Solving any unsolved sudoku puzzle is done here, first call generates a solved puzzle
#Uses a backtracking algorithm 

def Solve_Sudoku(board,not_check):
    x=Find_Empty_Cell(board)
    if x[2]==0:
        return True
    else:
        row=x[0]
        col=x[1]
        for i in np.random.permutation(10):
            if i!=0 and i!=not_check:
                if Check_Validity(board,row,col,i):
                    board[row,col]=i
                    if Solve_Sudoku(board,not_check):
                        return True
                    board[row,col]=0 
    return False

#Inputs difficulty and initializes playing board

def main():
    ch=int(input("Hello!Choose the level of difficulty-\n1.Easy\n2.Medium\n3.Hard\nYour choice:"))
    if ch==1:
        difficulty="Easy"
    elif ch==2:
        difficulty="Medium"
    else:
        difficulty="Hard"
    board=np.zeros((9,9),dtype="int8")
    if Solve_Sudoku(board,-1):
        Solved_Board=board.copy()
        print("\n\nThe unsolved puzzle is:\n")
        Generate_Unsolved_Puzzle(board,difficulty)
        Print_Board(board)
        Unsolved_Board=board.copy()
        Play_Sudoku(Solved_Board,Unsolved_Board)
    else:
        print("The board is not possible!")
    return

if __name__=="__main__":
    main()
