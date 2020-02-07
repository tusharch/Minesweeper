from board import Board
import argparse

def main(n, num_mines):
    # TODO: Write commandline game
    main_board = Board(n, num_mines)
    main_board.print_board()
    while(main_board.game!= "Game Over"):
        row = int(input("Enter row index(0-" +str(n - 1) + "):"))
        col = int(input("Enter column index(0-" +str(n - 1) + "):"))
        main_board.move(row, col)

# DO NOT EDIT--------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='?', type=int, default=10)
    parser.add_argument('num_mines', nargs='?', type=int, default=10)
    return parser.parse_args() 

if __name__ == "__main__":
    args = parse_args()
    main(args.n, args.num_mines)

# DO NOT EDIT--------------------------------------------
