class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        curSum = ans = 0
        for i, num in enumerate(nums):
            curSum += num
            counter[num] += 1
            if i >= k:
                prev = nums[i-k]
                curSum -= prev
                counter[prev] -= 1
                if counter[prev] == 0:
                    del counter[prev]
            if len(counter) == k:
                ans = max(ans, curSum)
        return ans