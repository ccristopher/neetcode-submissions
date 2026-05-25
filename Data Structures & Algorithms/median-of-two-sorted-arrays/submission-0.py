class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            one, two = nums1, nums2
        else:
            one, two = nums2, nums1
        
        total = len(one) + len(two)
        half = total // 2

        l, r = 0, len(one) - 1
        while True:
            i = (l + r) // 2 if l <= r else -1
            j = half - i - 2

            oneMin = one[i] if i >= 0 else float("-inf")
            oneMax = one[i + 1] if (i + 1) < len(one) else float("inf")
            twoMin = two[j] if j >= 0 else float("-inf")
            twoMax = two[j + 1] if (j + 1) < len(two) else float("inf")

            if oneMin <= twoMax and twoMin <= oneMax:
                if total % 2:
                    return float(min(oneMax, twoMax))
                return (max(oneMin, twoMin) + min(oneMax, twoMax)) / 2.0
            elif oneMin > twoMax:
                r = i - 1
            else:
                l = i + 1