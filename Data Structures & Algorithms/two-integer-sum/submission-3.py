class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in my_hash:
                return [my_hash[j], i]
            my_hash[nums[i]] = i