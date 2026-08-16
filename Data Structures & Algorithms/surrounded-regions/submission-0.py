class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])


        def markUnreachable(board, row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if board[row][col] == 'X' or board[row][col] == '-':
                return

            board[row][col] = '-' # Mark visited
            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for dx, dy in directions:
                markUnreachable(board, row+dx, col+dy)

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows -1 or col == 0 or col == cols - 1) and board[row][col] == 'O':
                    markUnreachable(board, row, col)
        print(board)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '-':
                    board[row][col] = 'O'
        