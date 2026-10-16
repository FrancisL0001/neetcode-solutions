class Solution(object):
    def groupAnagrams(self, strs : list[str]) -> list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = defaultdict(list)

        for s in strs:
            key = self.getKey(s)

            anagrams[key].append(s)

        return list(anagrams.values())



    def getKey(self, val : str) -> tuple[int]:
        key = [0 for _ in range(26)]

        for v in val:
            key[ord(v) - ord('a')] += 1

        return tuple(key)