class Solution:
    def shareCandies(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        totalUnique = len(counter)
        ans = 0
        for i in range(len(nums)):
            counter[nums[i]] -= 1
            if counter[nums[i]] == 0:
                del counter[nums[i]]
            if i >= k:
                counter[nums[i - k]] += 1
            if i >= k - 1:
                ans = max(ans, len(counter))
        return ans