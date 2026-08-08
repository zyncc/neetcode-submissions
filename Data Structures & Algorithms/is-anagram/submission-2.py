from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)

        for char in s:
            dic[char] += 1

        for char in t:
            dic[char] -= 1

        for value in dic.values():
            if value != 0:
                return False

        return True