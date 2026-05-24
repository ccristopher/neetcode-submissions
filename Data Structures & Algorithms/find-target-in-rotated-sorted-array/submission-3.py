class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                # numbers smaller than m smaller than r on the left, bigger than r on the right, bigger than m: smaller than r on the right, bigger than r on the left
                if target < nums[m]:
                    if target < nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                elif target > nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                
                else:
                    return m
            
            else:
                # numbers smaller than m smaller than r on the right, bigger than r on the left, bigger than m: smaller than r on the left, bigger than r on the right
                if target < nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                elif target > nums[m]:
                    if target < nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                
                else:
                    return m
            
        return -1