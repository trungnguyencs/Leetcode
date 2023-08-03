class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #time: O(n) - space: O(n)
        # return len(nums) > len(set(nums))
    
        #time: O(nlogn) - space: O(1)
        nums.sort()
        return any(nums[i] == nums[i+1] for i in range(len(nums) - 1))