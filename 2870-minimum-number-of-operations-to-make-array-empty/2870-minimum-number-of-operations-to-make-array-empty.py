class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        minOps = 0
        for num, freq in counter.items():
            if freq == 1: return -1
            if freq % 3 == 0:
                minOps += freq//3
            elif freq % 3 == 2:
                minOps += freq//3 + 1
            else:
                minOps += (freq - 4)//3 + 2
        return minOps