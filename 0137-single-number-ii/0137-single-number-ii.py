class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in counter:
            if counter[num] == 1: return num