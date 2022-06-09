class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = data.count(1)
        # find the window of size oneCount with the most numbers of 1s
        c = windowWithMostOnes = 0
        for i, num in enumerate(data):
            c += (num == 1)
            if i >= oneCount:
                c -= (data[i - oneCount] == 1)
            windowWithMostOnes = max(windowWithMostOnes, c)
        return oneCount - windowWithMostOnes