class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        cmp = functools.cmp_to_key(lambda x, y: int(x+y) - int(y+x))
        nums.sort(key=cmp, reverse=True)
        return '0' if nums[0] == '0' else ''.join(nums)