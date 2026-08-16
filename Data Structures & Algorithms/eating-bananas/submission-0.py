class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minRate = 1
        maxRate = max(piles)
        optimalRate = 1

        while minRate <= maxRate:
            rate = (minRate + maxRate) // 2
            if self.canBeEaten(piles, rate, h):
                optimalRate = min(rate, maxRate)
                maxRate = rate - 1
            else:
                minRate = rate + 1

        return optimalRate


    def canBeEaten(self, piles, rate, h):

        k = 0

        for p in piles:
            k += math.ceil(p/rate)
        
        return k <= h
        

        