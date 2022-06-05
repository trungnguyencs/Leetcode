class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # # swaps
        # swaps = {}
        # for s, e in reversed(operations):
        #     swaps[s] = swaps[e] if e in swaps else e
        # for i, num in enumerate(nums):
        #     if num in swaps:
        #         nums[i] = swaps[num]
        # return nums
        
        # index mapping
        dic = {num: i for i, num in enumerate(nums)}
        for s, e in operations:
            i = dic[s]
            nums[i] = e
            dic[e] = i
            del dic[s]
        return nums