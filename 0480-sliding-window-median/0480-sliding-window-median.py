class Solution:

    # #Solution 1: Maintain a sorted sliding window (using regular list)
    # #Runtime: O(klogk + nk) = O(nk)
    # from bisect import bisect
    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     window = []
    #     for i in range(k):
    #         window.append(nums[i])
    #     window.sort()
    #     ans = [self.getMedianFromSortedArray(window)]
    #     for i in range(k, len(nums)):
    #         lastNum = nums[i-k]
    #         lastNumIndex = bisect(window, lastNum) - 1
    #         del window[lastNumIndex]
    #         indexToInsert = bisect(window, nums[i])
    #         window.insert(indexToInsert, nums[i])
    #         ans.append(self.getMedianFromSortedArray(window))
    #     return ans

    #Solution 2: Maintain a sorted sliding window (using SortedList)
    #Runtime: O(nlogk)
    from sortedcontainers import SortedList
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        for i in range(k):
            window.add(nums[i])
        ans = [self.getMedianFromSortedArray(window)]
        for i in range(k, len(nums)):
            window.remove(nums[i-k])
            window.add(nums[i])
            ans.append(self.getMedianFromSortedArray(window))
        return ans

    def getMedianFromSortedArray(self, arr):
        n = len(arr)
        if n % 2 == 1:
            return arr[n//2]
        return (arr[n//2] + arr[n//2 - 1])/2