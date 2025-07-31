class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)
        ans = -1
        for num, freq in counter.items():
            if num == freq:
                ans = max(ans, num)
        return ans  