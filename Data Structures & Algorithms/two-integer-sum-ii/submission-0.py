class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1, pt2 = 0, len(numbers) - 1
        while pt1 < pt2:
            curr_sum = numbers[pt1] + numbers[pt2]
            if curr_sum == target:
                return [pt1 + 1, pt2 + 1]
            if curr_sum > target:
                pt2 -= 1
            else:
                pt1 += 1