class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find what row it is 

        low = 0
        high = len(matrix) - 1
        row = -1
        col = len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][col] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if row == -1:
            return False
    

        # Search the identified row  
        rowStart = 0
        rowEnd = len(matrix[row]) - 1

        while rowStart <= rowEnd:
            rowMid = (rowStart + rowEnd) // 2
            if matrix[row][rowMid] == target:
                return True
            elif  matrix[row][rowMid] < target:    
                rowStart = rowMid + 1
            else:
                rowEnd = rowMid - 1

        return False