class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        # # O(n): find min window size len(arr) - k and subtract
        # w = len(arr) - k
        # curSum = minSum = sum(arr[:w])
        # for i in range(w, len(arr)):
        #     curSum += arr[i] - arr[i-w]
        #     minSum = min(minSum, curSum)
        # return sum(arr) - minSum
    
        # O(k): find max window size k in the array containing k last and k first elements
        curSum = maxSum = sum(arr[-k:])
        for i in range(k):
            curSum += arr[i] - arr[-k+i]
            maxSum = max(maxSum, curSum)
        return maxSum