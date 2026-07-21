class Solution:
    def isPalindrome(self, s: str) -> bool:
        trans = s.lower().replace(' ', '')
        trans = re.sub(r'[^a-zA-Z0-9\s]', '', trans)
        i, j = 0, len(trans)-1

        while i <= j:
            if trans[i] != trans[j]:
                # print(trans[i], trans[j], trans)
                return False
            i += 1
            j -= 1
        return True