class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1]*len(nums)
        for i in range(1, len(nums)):
            L[i] = L[i-1]*nums[i-1]
        R = 1
        for i in range(len(nums)-2, -1, -1):
            R *= nums[i+1]
            L[i] *= R
        return L