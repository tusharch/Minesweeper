import random

class Board:
    def __init__(self, n, num_mines):
        self.n = n
        self.num_mines = num_mines
        self.board = []
        self.mines = set()
        self.game = "In Progress"
        for row in range(n):
            tempRow = []
            for col in range(n):
                tempRow.append("X")
            self.board.append(tempRow)
        
        for i in range(num_mines):
            row = random.randint(0,n - 1)
            col = random.randint(0,n - 1)
            pair = (row,col)
            while(pair in self.mines):
                row = random.randint(0,n - 1)
                col = random.randint(0,n - 1)
                pair = (row, col)
            print(pair)
            self.mines.add(pair)
    def print_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(self.board[row][col], end = " ")
            print('\n')
    
    def check_win(self):
        total_uncovered = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == "X":
                    total_uncovered +=1
        if total_uncovered == len(self.mines):
            self.game = "Game Over"
            print("You Win!!")


    def move(self, row, col):
        if (row, col) in self.mines:
            self.board[row][col] = "M"
            self.print_board()
            self.game = "Game Over"
            print("Game Over")
        else:
            print(type(row))
            if row > self.n - 1 or col > self.n - 1 or row < 0 or col < 0:
                print("Invalid Move")
            if self.board[row][col] != "X":
                print("Already Uncovered")
            num_adj_mines = 0
            if row > 0:
                if (row - 1,col) in self.mines:
                    num_adj_mines += 1
                if col > 0:
                    if (row - 1,col - 1) in self.mines:
                        num_adj_mines += 1
                if col < self.n - 1:
                    if (row - 1,col + 1) in self.mines:
                        num_adj_mines += 1
            if row < self.n - 1:
                if (row + 1,col) in self.mines:
                    num_adj_mines += 1
                if col > 0:
                    if (row + 1,col - 1) in self.mines:
                        num_adj_mines += 1
                if col < self.n - 1:
                    if (row + 1,col + 1) in self.mines:
                        num_adj_mines += 1
            if col > 0:
                if (row,col - 1) in self.mines:
                        num_adj_mines += 1
            if col < self.n - 1:
                if (row,col + 1) in self.mines:
                        num_adj_mines += 1
            
            self.board[row][col] = num_adj_mines
            self.print_board()
            self.check_win()





