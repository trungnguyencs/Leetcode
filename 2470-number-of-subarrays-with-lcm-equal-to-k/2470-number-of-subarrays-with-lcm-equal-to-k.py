class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for l in range(len(nums)):
            lcm = nums[l]
            for r in range(l, len(nums)):
                lcm = math.lcm(lcm, nums[r])
                if lcm == k: count += 1
                elif lcm > k: break
        return count