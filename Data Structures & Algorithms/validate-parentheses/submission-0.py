class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matcher = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in matcher:
                if not stack or stack[-1] != matcher[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0