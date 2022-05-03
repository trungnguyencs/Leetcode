class Solution:
    def average(self, salary: List[int]) -> float:
        largest, smallest, total = salary[0], salary[0], salary[0]
        for num in salary[1:]:
            total += num
            if num > largest: largest = num
            if num < smallest: smallest = num
        return (total-largest-smallest)/(len(salary)-2)