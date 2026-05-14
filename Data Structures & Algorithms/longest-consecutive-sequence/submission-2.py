class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            numbers.add(num)
        
        max_length = 0
        while len(numbers) != 0:
            num = numbers.pop()
            cur_length = 1
            i = 1
            while int(num + i) in numbers:
                cur_length += 1
                numbers.remove(num + i)
                i += 1
            i = 1
            while int(num - i) in numbers:
                cur_length += 1
                numbers.remove(num - i)
                i += 1
            
            max_length = max(cur_length, max_length)
        
        return max_length