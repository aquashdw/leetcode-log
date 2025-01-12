class MinStack:

    def __init__(self):
        self.head = 0
        self.stack = []
        self.min = None
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.stack) == self.head:
            self.stack.append(None)
        self.stack[self.head] = val
        if self.min is None or val < self.min:
            self.mins.append(self.head)
            self.min = self.stack[self.mins[-1]]
        self.head += 1

    def pop(self) -> None:
        self.head -= 1
        self.update_min()

    def top(self) -> int:
        return self.stack[self.head - 1]

    def update_min(self):
        if self.mins[-1] == self.head:
            self.mins.pop()
        if self.mins:
            self.min = self.stack[self.mins[-1]]
        else:
            self.min = None

    def getMin(self) -> int:
        if not self.mins:
            return None
        return self.min


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-1)
    print(min_stack.top())
    print(min_stack.getMin())
    min_stack.push(1)
    print(min_stack.top())
    print(min_stack.getMin())
