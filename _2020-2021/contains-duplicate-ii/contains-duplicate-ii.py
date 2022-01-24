class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        uniq = set()
        l = 0
        for r, num in enumerate(nums):
            if r - l > k:
                uniq.remove(nums[l])
                l += 1
            if num in uniq: return True
            uniq.add(num)
        return False