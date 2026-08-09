class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        leftBraces = ['(', '[', '{']

        for char in s:
            if char in leftBraces:
                stack.append(char)

            if len(stack) == 0:
                return False

            else:
                match char:
                    case ')':
                        if stack.pop() != '(':
                            return False 
                    case ']':
                        if stack.pop() != '[':
                            return False 
                    case '}':
                        if stack.pop() != '{':
                            return False 
        if len(stack) == 0:
            return True
        return False