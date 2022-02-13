# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y or not sea.hasShips(topRight, bottomLeft): return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y: return 1
        mx, my = (bottomLeft.x + topRight.x)//2, (bottomLeft.y + topRight.y)//2
        return self.countShips(sea, Point(mx, my), bottomLeft)\
            + self.countShips(sea, topRight, Point(mx + 1, my + 1))\
            + self.countShips(sea, Point(topRight.x, my), Point(mx + 1, bottomLeft.y))\
            + self.countShips(sea, Point(mx, topRight.y), Point(bottomLeft.x, my + 1))