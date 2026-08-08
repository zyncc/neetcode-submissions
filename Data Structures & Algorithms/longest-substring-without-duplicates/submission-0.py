class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            if s[right] not in seen:
                seen.add(s[right])
            
            longest = max(longest, (right - left) + 1)

        return longest