class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Go through rows
        for row in board:
            numbers = {}
            for cell in row:
                if cell != ".":
                    if numbers.has_key(cell):
                        return False
                    else:
                        numbers[cell] = 1
        
        # Go through columns
        for column in range(9):
            numbers = {}
            for row in range(9):
                if board[row][column] != ".":
                    if numbers.has_key(board[row][column]):
                        return False
                    else:
                        numbers[board[row][column]] = 1

        # Go through grid
        for grid_row in range(0, 9, 3):
            for grid_column in range(0, 9, 3):
                numbers = {}
                for row in range(grid_row, grid_row+3):
                    for col in range(grid_column, grid_column+3):
                        if board[row][col] != ".":
                            if numbers.has_key(board[row][col]):
                                return False
                            else:
                                numbers[board[row][col]] = 1

        return True
        
"""
Time complexity: O(n^2) 
Space complexity: O(n)
"""