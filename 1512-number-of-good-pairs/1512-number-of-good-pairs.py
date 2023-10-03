class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            ans += counter[num]
            counter[num] += 1
        return ans