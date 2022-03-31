class Solution:
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid 
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans   