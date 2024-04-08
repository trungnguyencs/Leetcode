class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        counter = Counter(students)
        i = 0
        while i < n and counter[sandwiches[i]] > 0:
            counter[sandwiches[i]] -= 1
            i += 1
        return n - i