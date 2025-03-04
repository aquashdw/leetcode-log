from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.count_dict = defaultdict(list)
        self.num_count = defaultdict(int)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.count_dict[self.num_count[val] + 1].append(val)
        self.num_count[val] += 1
        self.max_count = max(self.num_count[val], self.max_count)

    def pop(self) -> int:
        target_count = self.max_count
        if len(self.count_dict[target_count]) == 1:
            self.max_count -= 1

        val = self.count_dict[target_count].pop()
        self.num_count[val] -= 1

        return val


if __name__ == '__main__':
    freq_stack = FreqStack()
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(4)
    freq_stack.push(5)
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
