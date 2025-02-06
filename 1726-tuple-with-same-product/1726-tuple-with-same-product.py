class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counter[nums[i] * nums[j]] += 1
        # Choose 2 from freq pairs. Each pair has 8 tuple arrangements
        return 8 * sum(math.comb(freq, 2) for freq in counter.values())