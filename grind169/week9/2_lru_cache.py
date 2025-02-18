class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.prev.val if self.prev else self.prev} <- {self.val} -> {self.next.val if self.next else self.next}'


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.labels = {}
        self.front = Node(0, 'front')
        self.back = Node(-1, 'back')
        self.front.next = self.back
        self.back.prev = self.front

    def get(self, key: int) -> int:
        if key not in self.labels:
            return -1

        target = self.labels[key]
        tar_next, tar_prev = target.next, target.prev
        tar_prev.next = tar_next
        tar_next.prev = tar_prev
        target.prev, target.next = self.front, self.front.next
        target.next.prev = target
        self.front.next = target
        return target.val

    def put(self, key: int, value: int) -> None:
        node = self.labels[key] if key in self.labels else Node(key, value)
        if key in self.labels:
            node_prev, node_next = node.prev, node.next
            node_prev.next = node_next
            node_next.prev = node_prev
            node.val = value
        else:
            self.labels[key] = node

        front, second = self.front, self.front.next
        front.next, node.prev = node, front
        second.prev, node.next = node, second

        if len(self.labels) > self.capacity:
            remove = self.back.prev
            rem_next, rem_prev = remove.next, remove.prev
            rem_prev.next = rem_next
            rem_next.prev = rem_prev
            self.labels.pop(remove.key)

    def __str__(self):
        values = []
        node = self.front
        for _ in range(len(self.labels)):
            node = node.next
            values.append(node.val)

        return " - ".join(map(str, values))


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
