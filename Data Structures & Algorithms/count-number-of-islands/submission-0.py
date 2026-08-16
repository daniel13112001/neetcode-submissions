class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def markIslandVisited(grid, row, col):

            if row < 0 or col < 0:
                return
            if row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] == '0':
                return

            grid[row][col] = '0'

            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            for dx, dy in directions:
                markIslandVisited(grid, row+dx, col+dy)

        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    numIslands += 1
                    markIslandVisited(grid, row, col)

        return numIslands
        