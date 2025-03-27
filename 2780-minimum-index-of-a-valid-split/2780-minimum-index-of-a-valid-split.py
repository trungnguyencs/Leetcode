class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majorityNum = [num for num, freq in counter.items() if freq > len(nums)//2][0]
        count = 0
        for i, num in enumerate(nums):
            if num == majorityNum:
                count += 1
            if count > (i + 1)//2 and counter[majorityNum] - count > (len(nums) - (i + 1))//2:
                return i
        return -1