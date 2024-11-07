class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        # inorder for all AND to be > 0, there must be some bit that all numbers have 1s
        # => count frequencies of 1s in each bit position
        # the largest freq of all positions is the size of the largest satisfying combination
        counter = Counter()
        for num in nums:
            for i in range(32):
                counter[i] += num & 1
                num >>= 1
        return max(counter.values())