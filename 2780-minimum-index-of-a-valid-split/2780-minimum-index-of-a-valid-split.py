class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #O(n) space using hashmap is trivial
        #Here we find the majority element using only O(1) space by implementing the voting algo from 169. Majority Element
        majorityNum = self.findMajorityElement(nums)
        majorityNumFreq = self.findMajorityElementFreq(nums, majorityNum)
        count = 0
        for i, num in enumerate(nums):
            if num == majorityNum:
                count += 1
            if count > (i + 1)//2 and majorityNumFreq - count > (len(nums) - (i + 1))//2:
                return i
        return -1

    def findMajorityElement(self, nums):
        majorityNum = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majorityNum:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majorityNum = nums[i]
                    count = 1
        return majorityNum

    def findMajorityElementFreq(self, nums, majorityNum):
        count = 0
        for num in nums:
            if num == majorityNum:
                count += 1
        return count