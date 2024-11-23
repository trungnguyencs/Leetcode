class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R, C = len(box), len(box[0])
        ans = [['.']*R for _ in range(C)]
        for r in range(R):
            count = 0
            for c in range(C):
                if box[r][c] == '#':
                    count += 1
                elif box[r][c] == '*':
                    ans[c][r] = '*'
                    self.fill(ans, r, c-1 , count)
                    count = 0
            self.fill(ans, r, c, count)
        #ans is currently the transpose of box, i.e. row R-1 becomes col R-1
        #however, we want row R-1 becomes col 0, so we need to reverse column orders
        for row in ans:
            row.reverse()
        return ans
        
    def fill(self, ans, r, c, count):
        for _ in range(count):
            ans[c][r] = '#'
            c -= 1