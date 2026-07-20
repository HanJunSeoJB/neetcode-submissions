class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        answer = ""
        n = len(strs)
        for i in range(n):
            answer += " ".join([str(ord(ch)) for ch in strs[i]])
            if i < n - 1:
                answer += ","
        return answer

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        if not s:
            return [""]
        arr = s.split(',')
        answer = []
        for a in arr:
            if not a:
                answer.append("")
                continue
            tmp = a.split(' ')
            answer.append("".join([chr(int(t)) for t in tmp]))
        return answer