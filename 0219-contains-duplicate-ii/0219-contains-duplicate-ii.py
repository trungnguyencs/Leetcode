class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k: return True
            dic[num] = i
        return False