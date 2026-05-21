class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif not stack:
                return False
            elif not c == brackets[stack[-1]]:
                return False
            else:
                stack.pop()
        
        if stack:
            return False
        
        return True