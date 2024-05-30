class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # if a == b it means a ^ b == 0, so we need to find all subarrays that XOR to 0
        # every such subarray with N elements can be split into N-1 triplets
        # use nested loop to find all subarrays O(N^2) time, O(1) space
        res = 0
        for i in range(len(arr) - 1):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    res += j - i
        return res