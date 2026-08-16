
class Solution:

    def trap(self, height: List[int]) -> int:

        maxToTheLeft = []
        maxToTheRight = []

        for idx, h in enumerate(height):
            if idx == 0:
                maxToTheLeft.append(0)
            else:
                maxToTheLeft.append(max(maxToTheLeft[-1], height[idx-1]))
        

        for idx in range(len(height)-1, -1, -1):
            if idx == len(height)-1:
                maxToTheRight.append(0)
            else:
                maxToTheRight.append(max(maxToTheRight[-1], height[idx+1]))
        
        out = []
        totalArea = 0
        n = len(height)

        for idx in range(n):
            print(maxToTheLeft[idx], maxToTheRight[n-1-idx], height[idx])
            area = min(maxToTheLeft[idx], maxToTheRight[n-1-idx]) - height[idx]
            if area > 0:
                totalArea += area

        return totalArea


        