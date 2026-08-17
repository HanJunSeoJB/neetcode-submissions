class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in dct:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != dct[ch]:
                    return False
            else:
                stack.append(ch)
        
        print(stack)
        if len(stack) > 0:
            return False

        return True