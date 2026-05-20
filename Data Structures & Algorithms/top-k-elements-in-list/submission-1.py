class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for key, value in freq.items():
            bucket[value].append(key)
        
        output = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                output.append(j)
                if len(output) == k:
                    return output