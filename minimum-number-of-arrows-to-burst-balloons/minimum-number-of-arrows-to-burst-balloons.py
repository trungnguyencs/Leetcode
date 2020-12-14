class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        print(points)
        count = 1
        _, cur_e = points[0]
        for s, e in points[1:]:
            if s > cur_e:
                count += 1
                cur_e = e
            else:
                cur_e = min(cur_e, e)
        return count
                
