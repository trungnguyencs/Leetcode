class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        curSum = ans = 0
        for num in nums:
            curSum += num
            ans += prefixSum[curSum - goal]
            prefixSum[curSum] += 1
        return ans