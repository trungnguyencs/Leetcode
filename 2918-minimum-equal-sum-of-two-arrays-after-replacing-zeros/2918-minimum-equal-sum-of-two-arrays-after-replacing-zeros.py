class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        c1 = nums1.count(0)
        c2 = nums2.count(0)
        if c1 == 0 and s2 + c2 > s1: return -1
        if c2 == 0 and s1 + c1 > s2: return -1
        return max(s1 + c1, s2 + c2)