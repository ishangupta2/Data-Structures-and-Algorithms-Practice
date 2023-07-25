class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            chars = [0]*26
            for c in word:
                chars[ord(c)-ord('a')] += 1
            group[tuple(chars)].append(word)
        return group.values()

