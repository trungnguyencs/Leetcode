# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n + 1
        while l < r:
            m = (l + r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l