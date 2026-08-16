class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSeen = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(prices[i]-minSeen, maxProfit)
            minSeen = min(prices[i], minSeen)

        return maxProfit
        