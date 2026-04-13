from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cols = defaultdict(list)
        for st in strs:
            cols["".join(sorted(st))].append(st)
        return list(cols.values())
