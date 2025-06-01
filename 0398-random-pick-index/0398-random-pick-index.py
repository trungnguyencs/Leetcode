class Solution:

    def __init__(self, nums: List[int]):
        self.numToIndexes = defaultdict(list)
        for i, num in enumerate(nums):
            self.numToIndexes[num].append(i)

    def pick(self, target: int) -> int:
        arr = self.numToIndexes[target]
        i = randint(0, len(arr) - 1)
        return arr[i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)