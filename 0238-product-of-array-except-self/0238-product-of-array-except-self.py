class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1]*n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        R = [1]*n
        for i in range(n - 2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
            L[i] *= R[i]
        return L