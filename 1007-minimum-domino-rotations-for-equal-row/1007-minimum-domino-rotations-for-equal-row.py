class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countA, countB, countSame = Counter(), Counter(), Counter()
        for a, b in zip(tops, bottoms):
            countA[a] += 1
            countB[b] += 1
            if a == b: countSame[a] += 1
        for a in countA:
            if countA[a] + countB[a] - countSame[a] == len(tops):
                return min(countA[a] - countSame[a], countB[a] - countSame[a])
        return -1