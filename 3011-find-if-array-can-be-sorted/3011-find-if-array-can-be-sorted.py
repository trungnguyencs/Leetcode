class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax = float('-inf')
        curMin = curMax = nums[0]
        prevBits = self.countBits(nums[0])
        for num in nums:
            bits = self.countBits(num)
            if bits != prevBits:
                prevMax = curMax
                curMin = curMax = num
                prevBits = bits
            curMin = min(curMin, num)
            curMax = max(curMax, num)
            if curMin < prevMax: return False     
        return True
    
    def countBits(self, num):
        bits = 0
        while num:
            bits += num & 1
            num >>= 1
        return bits