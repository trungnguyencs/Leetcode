class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r)//2
            neededOps = self.neededOps(nums, m)
            if neededOps > maxOperations:
                l = m + 1
            else:
                r = m - 1
        return l
        
    #Number of ops needed such that nums can be broken into numbers of at most maxVal
    def neededOps(self, nums, val):
        ops = 0
        for num in nums:
            if num % val == 0:
                ops += num//val - 1
            else:
                ops += num//val
        return ops