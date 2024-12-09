class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        goodPairs = [0]*len(nums)
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i-1] % 2:
                goodPairs[i] = goodPairs[i-1] + 1
        return [goodPairs[e] - goodPairs[s] == e - s for s, e in queries]