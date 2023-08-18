class TNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TNode()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def back(i, cur):
            if i==len(word):
                return cur.end
            if word[i] == '.':
                for n in cur.children:
                    if back(i+1, cur.children[n]):
                        return True
                return False

            if word[i] not in cur.children:
                return False
            return back(i+1, cur.children[word[i]])
        return back(0, curr)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)