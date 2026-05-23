class MinStack:
    def __init__(self):
        self.my_stack=[]
        self.my_min = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if not self.my_min or val <= self.my_min[-1]:
            self.my_min.append(val)

    def pop(self) -> None:
        val = self.my_stack.pop()
        if val == self.my_min[-1]:
            self.my_min.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.my_min[-1]