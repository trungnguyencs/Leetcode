class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = [[num, [num]] for num in nums]
        for i in range(len(arr)):
            for j in range(i):
                cur, curSet = arr[i]
                prev, prevSet = arr[j]
                if cur % prev == 0:
                    arr[i][1] = max(curSet, prevSet + [cur], key=len)
        return max([numSet for _, numSet in arr], key=len)