class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        
        suffix = [1] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = nums[i - 1] * suffix[i]
        
        output = [1] * len(nums)
        output[0] = suffix[1]
        output[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            output[i] = prefix[i - 1] * suffix[i + 1]
        
        return output