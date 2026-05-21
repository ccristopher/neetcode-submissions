class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_height = 0

        while l < r:
            if heights[l] <= heights[r]:
                max_height = max(max_height, heights[l] * (r - l))
                l += 1
            else:
                max_height = max(max_height, heights[r] * (r - l))
                r -= 1

        
        return max_height