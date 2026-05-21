class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        i, j = 0, 1
        
        i = prices[0]
        l = 0

        best = 0


        while j < len(prices):
            k = prices[j]
            if k <= i:
                i = k
                l = 0
            else:
                l = max(l, k)
                best = max(best, l - i)
            j += 1
        
        return best