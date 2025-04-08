class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        hasDuplicate = len([freq for freq in counter.values() if freq > 1])
        if hasDuplicate == 0: return 0
        steps = 0
        for i, num in enumerate(nums):
            if i % 3 == 0:
                steps += 1
            counter[num] -= 1
            if counter[num] == 1:
                hasDuplicate -= 1
                if hasDuplicate == 0: return steps