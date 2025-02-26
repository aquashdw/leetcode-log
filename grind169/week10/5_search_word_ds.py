class WordDictionary:

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        children = self.children
        for char in word:
            if char not in children:
                children[char] = {}
            children = children[char]
        children["_"] = None

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(children, next_idx):
            if not children:
                return False
            if next_idx == n:
                return "_" in children

            letter = word[next_idx]
            if letter != '.':
                return dfs(children.get(letter), next_idx + 1)

            for key in children:
                if dfs(children.get(key), next_idx + 1):
                    return True

            return False

        return dfs(self.children, 0)


if __name__ == '__main__':
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(word_dict.search("pad"))
    print(word_dict.search("bad"))
    print(word_dict.search(".ad"))
    print(word_dict.search("b.."))
