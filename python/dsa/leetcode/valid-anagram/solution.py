class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s increments and t decrements, so anagrams leave every counter at zero
        count = {}
        for a, b in zip(s, t, strict=True):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1

        return all(val == 0 for val in count.values())
