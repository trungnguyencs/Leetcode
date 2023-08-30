class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # last number will be the largest and thus should not be split
        last = nums[-1]
        ans = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= last: # no replacement
                last = nums[i]
            else:
                splits = nums[i]//last
                if nums[i] % last == 0: # ex: [6, 3] -> [3, 3, 3]
                    ans += splits - 1
                    last = nums[i]//splits
                else: # ex: [13, 6] -> [4, 4, 5, 6]
                    ans += splits
                    last = nums[i]//(splits + 1)
        return ans