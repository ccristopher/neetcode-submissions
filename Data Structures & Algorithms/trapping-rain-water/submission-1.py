class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = height[0]
        suffix[-1] = height[-1]

        water = 0

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
            if i != len(height) - 1:
                suffix[-i] = max(suffix[-(i - 1)], height[-i])
        
        print(prefix)
        print(suffix)
        
        for i in range(1, len(height) - 1):
            minimum = prefix[i - 1]
            maximum = suffix[i + 1]
            if height[i] < minimum and height[i] < maximum:
                water += (min(minimum, maximum) - height[i])
        
        return water