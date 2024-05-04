class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] + nums1[j] > nums2[i] + nums2[j] and i < j
        # -> nums1[i] - nums2[i] > nums2[j] - nums1[j] and i < j
        # -> diff[i] > -diff[j] and i < j
        # -> diff[i] + diff[j] > 0 (i, j don't matter)
        n = len(nums1)
        diff = [(num1 - num2) for num1, num2 in zip(nums1, nums2)]
        diff.sort()
        ans = 0
        for l, num in enumerate(diff):
            r = bisect_right(diff, -num, lo=l+1, hi=n)
            ans += n - r
        return ans