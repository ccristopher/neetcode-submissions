class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        largest = 0
        for i in nums_set:
            count = 1
            if i - 1 not in nums_set:
                j = 1
                while i + j in nums_set:
                    count += 1
                    j += 1
            if count > largest:
                largest = count
        
        return largest