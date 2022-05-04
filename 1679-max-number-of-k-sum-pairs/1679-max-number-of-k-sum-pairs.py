class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        return sum([min(counter[num], counter[k-num]) for num in counter if k-num in counter])//2