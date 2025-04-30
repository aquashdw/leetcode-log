import random


class RandomizedSet:

    def __init__(self):
        self.data_dict = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False

        self.data_dict[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_dict:
            return False

        replace_idx = self.data_dict[val]
        if replace_idx == len(self.data_list) - 1:
            self.data_dict.pop(val)
            self.data_list.pop()
            return True

        replace_val = self.data_list.pop()
        self.data_list[replace_idx] = replace_val
        self.data_dict[replace_val] = replace_idx
        self.data_dict.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == '__main__':
    solution = RandomizedSet()
    print(solution.insert(1))
    print(solution.insert(2))
    print(solution.insert(3))
    print(solution.insert(2))
    print(solution.insert(3))
    print(solution.remove(3))
    print(solution.remove(3))
