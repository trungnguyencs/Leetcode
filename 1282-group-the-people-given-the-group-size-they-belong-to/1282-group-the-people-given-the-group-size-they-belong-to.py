class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        ans = []
        for i, groupSize in enumerate(groupSizes):
            dic[groupSize].append(i)
            if len(dic[groupSize]) == groupSize:
                ans.append(dic[groupSize])
                dic[groupSize] = []
        return ans