class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        numRows = len(board)
        numCols = len(board[0])

        def dfs(row, col, start): #0,0,0 -> row, col, start

            if start >= len(word):
                return True

            if row >= numRows or col >= numCols:
                return False

            if row < 0 or col < 0:
                return False
            

            if board[row][col] != word[start]:
                return False
            
            if board[row][col] == 'X':
                return False

            # Mark visited
            tmp = board[row][col] #a
            board[row][col] = 'X'
            exists = (
                dfs(row, col+1, start+1) or 
                dfs(row, col-1, start+1) or 
                dfs(row+1, col, start+1)  or 
                dfs(row-1, col, start+1)
            )
            if exists:
                return True
            board[row][col] = tmp

        for row in range(numRows):
            for col in range(numCols):
                if board[row][col] == word[0]:
                    exists = dfs(row, col, 0)
                    if exists:
                        return True 
 
        return False
        



        