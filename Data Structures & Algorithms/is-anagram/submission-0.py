from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap1, hashMap2 = defaultdict(int), defaultdict(int)

        for char in s:
            hashMap1[char] += 1

        for char in t:
            hashMap2[char] += 1

        return hashMap1 == hashMap2