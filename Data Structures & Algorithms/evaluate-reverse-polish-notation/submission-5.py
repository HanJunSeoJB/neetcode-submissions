class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        if len(tokens) == 1:
            return int(tokens[-1])
        dct = {'+', '-', '/', '*'}

        def cal(a, b, op):
            match op:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return int(a / b)

        for tk in tokens:
            if tk in dct:
                b = nums.pop()
                a = nums.pop()
                nums.append(cal(int(a), int(b), tk))
            else:
                nums.append(tk)
            
        return nums[-1]

            