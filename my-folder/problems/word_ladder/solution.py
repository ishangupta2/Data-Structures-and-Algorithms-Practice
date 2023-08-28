class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pre = word[:i] + "*" + word[i+1:]
                nei[pre].append(word)
        visit = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while(queue):
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for m in range(len(word)):
                    pre = word[:m] + "*" + word[m+1:]
                    for w in nei[pre]:
                        if w not in visit:
                            queue.append(w)
                            visit.add(w)
            res += 1
        return 0
