class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return False
        else:
            if self.stack[len(self.stack)-1] == self.min_stack[len(self.min_stack)-1]:
                del self.min_stack[len(self.min_stack)-1]
            del self.stack[len(self.stack)-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]     
