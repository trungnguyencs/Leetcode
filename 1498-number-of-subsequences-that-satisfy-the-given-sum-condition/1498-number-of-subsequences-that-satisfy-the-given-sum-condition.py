class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                #2^(r - l) because each number in range[l + 1, r] can either exists not not exists in the subsequence
                ans += 2**(r - l)
                l += 1
        return ans % (10**9 + 7)