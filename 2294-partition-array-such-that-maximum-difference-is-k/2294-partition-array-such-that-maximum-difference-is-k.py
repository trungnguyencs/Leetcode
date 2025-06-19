class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        segmentCount = 1
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - m > k:
                segmentCount += 1
                m = nums[i]
        return segmentCount