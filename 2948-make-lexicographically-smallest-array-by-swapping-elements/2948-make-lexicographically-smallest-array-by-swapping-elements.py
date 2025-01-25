class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        #sort nums => we can find the group for each number
        #then sort the numbers in each group
        sortedNums = sorted(nums)
        numToGroup = {}
        groupToNumList = defaultdict(list)
        group = 0
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] - sortedNums[i-1] > limit:
                group += 1
            numToGroup[sortedNums[i]] = group
            groupToNumList[group].append(sortedNums[i])
        #sort the numbers in each group
        for numList in groupToNumList.values():
            numList.sort(reverse=True)
        #update ans
        for i, num in enumerate(nums):
            group = numToGroup[num]
            nums[i] = groupToNumList[group].pop()
        return nums