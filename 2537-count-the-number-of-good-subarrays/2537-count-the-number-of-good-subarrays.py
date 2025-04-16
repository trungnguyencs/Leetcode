class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = ans = goodPairs = 0
        counter = Counter()
        #For each right, find the furthest left that makes the window unsatisfied => every index before that left will satisfy
        for r, num in enumerate(nums): 
            goodPairs += counter[num]
            counter[num] += 1
            while goodPairs >= k:
                goodPairs -= counter[nums[l]] - 1
                counter[nums[l]] -= 1
                l += 1
            ans += l #then all start indices from [0, l-1] would form good subarrays
        return ans