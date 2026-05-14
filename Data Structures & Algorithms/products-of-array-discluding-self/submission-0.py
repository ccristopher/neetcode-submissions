class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        if length == 1:
            return [0]
        multiples = [1] * length
        for i in range(1, length, 1):
            multiples[i] = multiples[i - 1] * nums[i - 1]
        multiples[0] = 0
        # 0,1,2,8

        multiples2 = [1] * length
        for i in range(length - 1, 0, -1):
            multiples2[i - 1] = multiples2[i] * nums[i]
        multiples2[length - 1] = 0
        # 48 24 6 0

        output = []
        output.append(multiples2[0])
        for i in range(1, length - 1, 1):
            output.append(multiples[i] * multiples2[i])
        output.append(multiples[-1])
        return output
        # for multiple in multiples:
            # [1, 2, 8, 48]

        # if len(nums) == 0:
        #     return [0]
        # output = [1] * len(nums)
        # for i in range(len(nums)):

        #     output[i]