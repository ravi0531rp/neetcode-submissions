from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        
        max_list = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in store.items():
            max_list[freq].append(num)

        fin_out = []
        for bucket in reversed(max_list):
            for num in bucket:
                fin_out.append(num)
                if len(fin_out) == k:
                    return fin_out
        return fin_out