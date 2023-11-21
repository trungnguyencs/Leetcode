class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            key = num - self.reverseNumber(num)
            ans += counter[key]
            counter[key] += 1
        return ans % (10**9 + 7)
        
    def reverseNumber(self, num):
        reversedNum = 0
        while num:
            d = num % 10
            num //= 10
            reversedNum = reversedNum * 10 + d
        return reversedNum