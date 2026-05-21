class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4, -1, -1, 0, 1, 2

        output = []

        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                else:
                    output.append([nums[k], nums[i], nums[j]])
                    i += 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        
        return output