class MinStack:

    def __init__(self):
        self.stack = []
        self.ms = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.ms) == 0 or val < self.ms[-1]:
            self.ms.append(val)
        else:
            self.ms.append(self.ms[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ms[-1]
