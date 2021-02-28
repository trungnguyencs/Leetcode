class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2: return 0
        elif s1 < s2: return self.helper(nums1, nums2, s2 - s1)
        return self.helper(nums2, nums1, s1 - s2)
    
    def helper(self, small, large, diff):
        small.sort(); large.sort(reverse=True)
        i = j = 0
        while True:
            increment = 6 - small[i] if i < len(small) else 0
            decrement = large[j] - 1 if i < len(large) else 0
            if increment == decrement == 0: return -1
            if increment >= decrement:
                diff -= increment
                i += 1
            else:
                diff -= decrement
                j += 1
            if diff <= 0: return i + j