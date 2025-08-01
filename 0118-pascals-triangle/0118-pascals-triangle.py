class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        for _ in range(numRows - 1):
            last = ans[-1]
            ans.append([a + b for a, b in zip(last + [0], [0] + last)])
        return ans      