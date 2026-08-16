class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        cheapestSeen = prices[0]
        bestProfit = 0

        for i in range(1, len(prices)):
            if prices[i] - cheapestSeen > bestProfit:
                bestProfit = prices[i] - cheapestSeen 
            if prices[i] < cheapestSeen:
                cheapestSeen = prices[i]

        return bestProfit

        