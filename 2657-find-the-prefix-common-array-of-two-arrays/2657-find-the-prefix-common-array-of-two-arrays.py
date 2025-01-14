class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA, setB = set(), set()
        ans = [0]*len(A)
        commons = 0
        for i, (a, b) in enumerate(zip(A, B)):
            if a == b:
                commons += 1
            else:
                if a in setB:
                    commons += 1
                if b in setA:
                    commons += 1
                setA.add(a)
                setB.add(b)
            ans[i] = commons
        return ans