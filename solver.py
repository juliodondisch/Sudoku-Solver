class Solution:

    def solve(self, board):
        # recursive
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                if value == ".":
                    # make list of all numbers 1-9
                    valid_nums = [str(i+1) for i in range(9)]
                    
                    # check numbers in the same row, column, and square
                    # eliminate numbers that already appear in any of these
                    
                    # row
                    for val in row:
                        if val in valid_nums:
                            valid_nums.remove(val)
                    
                    # column
                    for col in board:
                        if col[col_idx] in valid_nums:
                            valid_nums.remove(col[col_idx])
                    
                    # square
                    top = row_idx - row_idx % 3
                    bottom = row_idx + 2 - row_idx % 3
                    left = col_idx - col_idx % 3
                    right = col_idx + 2 - col_idx % 3

                    for i in range(left, right + 1):
                        for j in range(top, bottom + 1):
                            if board[j][i] in valid_nums:
                                valid_nums.remove(board[j][i])
                    
                    # solve sudoku with the first available number at that index of our board.
                    # if solve succeeds, return the solved board.
                    # if solve fails, then remove that number from the board and try another one.
                    for i in valid_nums:
                        board[row_idx][col_idx] = str(i)
                        if self.solve(board) != [["x"]]:
                            return board
                        
                    board[row_idx][col_idx] = "."
                    return [["x"]]
        return board

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solve(board)  # Do not return the board; just modify it in place
