class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            numbers.add(num)
        
        print(numbers)
        max_length = 0
        while len(numbers) != 0:
            num = numbers.pop()
            print(num)
            cur_length = 1
            i = 1
            print(num + i)
            while int(num + i) in numbers:
                print("did a thing")
                cur_length += 1
                numbers.remove(num + i)
                i += 1
            i = 1
            while int(num - i) in numbers:
                print("did a thing")
                cur_length += 1
                numbers.remove(num - i)
                i += 1
            
            print(numbers)
            print(max_length)
            print(cur_length)
            max_length = max(cur_length, max_length)
            print(max_length)
        
        return max_length