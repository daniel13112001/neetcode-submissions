class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestSeen = prices[0]
        bestProfit = 0

        for i, price in enumerate(prices):
            profit = price - cheapestSeen
            bestProfit = max(profit, bestProfit)
            cheapestSeen = min(price, cheapestSeen)

        return bestProfit
        