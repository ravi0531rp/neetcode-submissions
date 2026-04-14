class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for idx, num in enumerate(nums):
            if target - num in sums.keys():
                return [sums[target - num], idx]
            else:
                sums[num] = idx
        return []