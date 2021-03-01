class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums2) - sum(nums1)
        if diff < 0: return self.minOperations(nums2, nums1)
        counter = Counter([6-x for x in nums1] + [x-1 for x in nums2])
        i, steps = 5, 0
        while diff > 0:
            if i == 0: return -1
            if counter[i] == 0:
                i -= 1
            else:
                diff, counter[i], steps = diff-i, counter[i]-1, steps+1
        return steps