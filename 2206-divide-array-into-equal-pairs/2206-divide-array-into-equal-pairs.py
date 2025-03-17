class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(freq % 2 == 0 for freq in counter.values())