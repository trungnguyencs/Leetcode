class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = Counter({0: 1})
        curSum = ans = 0
        for num in nums:
            curSum += num
            ans += dic[curSum % k]
            dic[curSum % k] += 1
        return ans