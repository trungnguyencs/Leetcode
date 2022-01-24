class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # the answer is (k + # of numbers in array that is <= k)
        for num in arr:
            if num > k: return k
            k += 1
        return k
