class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1]*len(nums) #length of LIS ending at i
        count = [1]*len(nums) #count of LIS ending at i
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] < 1 + length[j]: # new longest LIS
                        length[i] = 1 + length[j]
                        count[i] = count[j]
                    elif length[i] == 1 + length[j]: # same length LIS
                        count[i] += count[j]
        maxLen = max(length)
        return sum(c for c, l in zip(count, length) if l == maxLen)