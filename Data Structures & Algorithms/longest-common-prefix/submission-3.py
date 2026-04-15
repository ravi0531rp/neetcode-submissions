from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for item in strs:
            if item == "":
                return ""

            j = 0
            min_traversal = min(len(prefix), len(item))
            smaller = prefix if len(prefix) < len(item) else item

            while j < min_traversal:
                if item[j] == prefix[j]:
                    j += 1
                else:
                    prefix = prefix[:j]
                    break
            if j == min_traversal:
                prefix = smaller
        return prefix
