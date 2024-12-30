class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        while len(self.stack_in) > 1:
            self.stack_out.append(self.stack_in.pop())
        value = self.stack_in.pop()
        while len(self.stack_out) > 0:
            self.stack_in.append(self.stack_out.pop())
        return value

    def peek(self) -> int:
        while len(self.stack_in) > 1:
            self.stack_out.append(self.stack_in.pop())
        value = self.stack_in.pop()
        self.stack_out.append(value)
        while len(self.stack_out) > 0:
            self.stack_in.append(self.stack_out.pop())
        return value

    def empty(self) -> bool:
        return len(self.stack_in) == 0


if __name__ == '__main__':
    queue = MyQueue()
    print(queue.empty())
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
