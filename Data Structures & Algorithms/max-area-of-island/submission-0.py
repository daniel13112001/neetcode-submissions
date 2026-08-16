class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0

        def calculateArea(grid, row, col) -> int:

            if row < 0 or col < 0:
                return 0
            
            if row >= len(grid) or col >= len(grid[0]):
                return 0
            
            if grid[row][col] == 0:
                return 0

            if grid[row][col] == 1:
                grid[row][col] = 0
                return (
                    1 + calculateArea(grid, row+1, col)
                    + calculateArea(grid, row-1, col)
                    + calculateArea(grid, row, col+1)
                    + calculateArea(grid, row, col-1)
                )
        
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = calculateArea(grid, row, col)
                    maxArea = max(area, maxArea)
                    print(area, maxArea)
        return maxArea