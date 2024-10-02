class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = -1
        for num, freq in counter.items():
            if freq == 1 and num > ans:
                ans = num
        return ans