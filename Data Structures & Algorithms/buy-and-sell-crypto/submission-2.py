class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = prices[0]
        j = 1
        best = 0

        l = 0
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