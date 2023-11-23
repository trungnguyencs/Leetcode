class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # bruteforce sort each subarr of each query O(m*nlogn)
        # another solution: each subarr find max, min and check if each element in the steps in the set of subarr O(m*n)
        return [self.isArithmSequence(nums, i, j) for i, j in zip(l, r)]
        
    def isArithmSequence(self, nums, l, r):
        s = set(nums[l:r+1])
        m, M = min(s), max(s)
        if (M - m) % (r - l) != 0: return False
        step = (M - m)//(r - l)
        return all((m + step*i) in s for i in range(r - l))