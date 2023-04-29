# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        L = reader.length()
        same3, notSame3 = 1, 0
        notSame3Idx = -1
        res0123 = reader.query(0, 1, 2, 3)
        # find numbers same as 3 and not same as by comparing 0123 to 012i (i > 3)
        for i in range(4, L):
            if reader.query(0, 1, 2, i) == res0123:
                same3 += 1
            else:
                notSame3 += 1
                notSame3Idx = i
        # find among 0, 1, 2 which ones are same as 3 by comparing with 0124
        res0124 = reader.query(0, 1, 2, 4)
        for i, (a, b, c, d) in enumerate([(1, 2, 3, 4), (0, 2, 3, 4), (0, 1, 3, 4)]):
            if reader.query(a, b, c, d) == res0124:
                same3 += 1
            else:
                notSame3 += 1
                notSame3Idx = i
        print(same3, notSame3)
        return -1 if same3 == notSame3 else 3 if same3 > notSame3 else notSame3Idx