from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            c = "".join(sorted(s))
            print(c)
            answer[c].append(s)
        return list(answer.values())