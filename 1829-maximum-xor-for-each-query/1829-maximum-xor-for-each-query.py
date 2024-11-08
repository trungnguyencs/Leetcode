class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxNum = 2**maximumBit - 1
        xor = 0
        ans = []
        for num in nums:
            xor ^= num
            ans.append(maxNum ^ xor) #a ^ b = maxNum => b = maxNum ^ a
        return ans[::-1]