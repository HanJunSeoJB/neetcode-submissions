class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        total_half = (len(nums1) + len(nums2) + 1) // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)

        while l <= r:
            i_A = (l + r) // 2
            i_B = total_half - i_A

            a_left = nums1[i_A - 1] if i_A > 0 else float("-inf")
            a_right = nums1[i_A] if i_A < len(nums1) else float("inf")

            b_left = nums2[i_B - 1] if i_B > 0 else float("-inf")
            b_right = nums2[i_B] if i_B < len(nums2) else float("inf")

            if a_left > b_right:
                r = i_A - 1
            elif b_left > a_right:
                l = i_A + 1
            else:
                if total % 2 == 0:
                    a_max = max(a_left, b_left)
                    b_min = min(a_right, b_right) 
                    return (a_max + b_min) / 2
                else:
                    return max(a_left, b_left)



