class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            r, c = q.popleft()

            neighbors = [(0,1), (0,-1), (-1,0), (1,0)]

            for nr, nc in neighbors:
                if r + nr < 0 or c + nc < 0 or r + nr >= rows or c + nc >= cols:
                    continue 
                if grid[r+nr][c+nc] == INF:
                    q.append((r+nr, c+nc))
                    grid[r+nr][c+nc] = grid[r][c] + 1

                




        