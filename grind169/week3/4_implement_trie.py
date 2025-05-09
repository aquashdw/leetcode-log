# iterative Trie
class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        children = self.children
        for char in word:
            if char not in children:
                children[char] = {}
            children = children[char]
        children["_"] = None

    def search(self, word: str) -> bool:
        children = self.children
        for char in word:
            if char not in children:
                return False
            children = children[char]
        return "_" in children

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for char in prefix:
            if char not in children.keys():
                return False
            children = children[char]
        return True


# recursive Trie
"""
class Trie:
    class Node:
        def __init__(self, value: str):
            self.value = value
            self.children = {}

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        if not word:
            return
        self.insert_recursive(word, 0, self.children)

    def insert_recursive(self, word: str, idx: int, children: Dict):
        if idx < len(word):
            letter = word[idx]
        else:
            letter = "_"

        if letter not in children:
            children[letter] = Trie.Node(letter)

        if letter == "_":
            return
        self.insert_recursive(word, idx + 1, children[letter].children)

    def search(self, word: str) -> bool:
        if not word:
            return True
        return self.search_recursive(word, 0, self.children)

    def search_recursive(self, word: str, idx: int, children: Dict) -> bool:
        if idx == len(word):
            return "_" in children

        letter = word[idx]
        if letter not in children
            return False

        return self.search_recursive(word, idx + 1, children[letter].children)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        return self.prefix_recursive(prefix, 0, self.children)

    def prefix_recursive(self, prefix: str, idx: int, children: Dict) -> bool:
        if len(prefix) == idx:
            return True

        letter = prefix[idx]
        if letter not in children.keys():
            return False

        return self.prefix_recursive(prefix, idx + 1, children[letter].children)
"""

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    print(trie.startsWith("apd"))
