class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        return self.merge(self.sortArray(nums[:len(nums)//2]), self.sortArray(nums[len(nums)//2:]))
        
    def merge(self, sorted1, sorted2):
        merged = []
        i = j = 0
        while i < len(sorted1) and j < len(sorted2):
            if sorted1[i] < sorted2[j]:
                merged.append(sorted1[i])
                i += 1
            else:
                merged.append(sorted2[j])
                j += 1
        merged += sorted1[i:] if j == len(sorted2) else sorted2[j:]
        return merged