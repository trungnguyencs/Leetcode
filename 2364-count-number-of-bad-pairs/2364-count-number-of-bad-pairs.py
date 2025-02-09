class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        goodPairs = 0
        for i, num in enumerate(nums):
            goodPairs += dic[num - i]
            dic[num - i] += 1
        return n * (n-1)//2 - goodPairs