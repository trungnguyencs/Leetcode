class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #equivalent to finding the smallest subarray with same reminder with sum(nums) of modulo p
        r = sum(nums) % p
        if r == 0: return 0
        dic = {0: -1}
        curSum = 0
        ans = float('inf')
        for i, num in enumerate(nums):
            curSum += num
            if (curSum - r) % p in dic:
                ans = min(ans, i - dic[(curSum - r) % p])
            dic[curSum % p] = i
        return -1 if ans >= len(nums) else ans