class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        #Bruteforce: applying each query & check all zeros takes O(N)
        #For K queries -> overall O(KN)
        #Instead: Binary search on the number of needed queries
        #To check for all zeros after k queries: use the same approach as 370. Range Addition, which takes O(K + N)
        #-> Overall O(logK * (K+N))
        if all(num == 0 for num in nums): return 0
        l, r = 0, len(queries)
        while l <= r:
            m = (l + r)//2
            canMakeAllZeroes = self.rangeAdditionAndCheckZeroes(nums, queries, m)
            if not canMakeAllZeroes:
                l = m + 1
            elif not self.rangeAdditionAndCheckZeroes(nums, queries, m - 1):
                return m
            else:
                r = m - 1
        return -1

    def rangeAdditionAndCheckZeroes(self, nums, queries, k):
        update = [0]*(len(nums) + 1)
        for i in range(k):
            l, r, val = queries[i]
            update[l] += val
            update[r + 1] -= val
        carry = 0
        for i, num in enumerate(nums):
            carry += update[i]
            if num > carry: return False
        return True