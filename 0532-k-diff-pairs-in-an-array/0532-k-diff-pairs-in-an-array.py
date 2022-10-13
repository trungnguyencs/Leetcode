class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if k == 0: 
            return sum(val > 1 for val in counter.values())
        return sum(x + k in counter for x in counter)