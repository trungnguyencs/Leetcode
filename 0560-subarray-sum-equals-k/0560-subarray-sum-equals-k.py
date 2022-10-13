class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter({0: 1})
        count = total = 0
        for num in nums:
            total += num
            count += counter[total - k]
            counter[total] += 1
        return count