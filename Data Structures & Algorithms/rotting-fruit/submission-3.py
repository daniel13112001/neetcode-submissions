class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        time = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
        
        while q:

            row, col = q.popleft()

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for dx, dy in directions:
                if row+dx < 0 or col+dy < 0 or row+dx >= rows or col+dy >= cols:
                    continue
                if grid[row+dx][col+dy] == 1:
                    q.append((row+dx, col+dy))
                    grid[row+dx][col+dy] = grid[row][col] + 1
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1 
                time = max(time, grid[row][col])
                
        print(f"time is {time}")
        if time <= 0:
            return time 
        return time - 2

        
                
