class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        pattern = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] > nums[i-1] and (not pattern or pattern[-1] != 'I'):
                    pattern.append('I')
            if nums[i] < nums[i-1] and (not pattern or pattern[-1] != 'D'):
                    pattern.append('D')        
            if len(pattern) > 3:
                return False
        return ''.join(pattern) == 'IDI'