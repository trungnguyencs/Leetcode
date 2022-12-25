class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        ans = [0]*len(queries)
        for i, q in enumerate(queries):
            ans[i] = bisect_right(nums, q)
        return ans