class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if k == 0: return sum([1 for key, val in counter.items() if val > 1])
        count = sum([1 for x in counter if x + k in counter])
        return count