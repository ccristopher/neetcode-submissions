class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        l, r = 1, max_k
        while l <= r:
            mid = l + (r - l) // 2
            
            mid_val = 0
            for pile in piles:
                mid_val += (pile + mid - 1) // mid
            
            if mid_val > h:
                l = mid + 1
            
            elif mid_val <= h:
                r = mid - 1
        
        return l