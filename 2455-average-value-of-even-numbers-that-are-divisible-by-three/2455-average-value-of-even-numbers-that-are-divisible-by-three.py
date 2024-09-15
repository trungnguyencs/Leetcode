class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = count = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1
        return 0 if count == 0 else total//count