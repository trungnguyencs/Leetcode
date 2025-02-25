class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        #the difference between an odd prefix sum and an even prefix sum will be an odd subarray
        #so we find the #odd prefix sums and #even prefix sums and multiply them
        oddPrefixSums, evenPrefixSums = 0, 1
        curSum = 0
        for num in arr:
            curSum += num
            if curSum % 2 == 1:
                oddPrefixSums += 1
            else:
                evenPrefixSums += 1
        return (oddPrefixSums * evenPrefixSums) % (10**9 + 7)