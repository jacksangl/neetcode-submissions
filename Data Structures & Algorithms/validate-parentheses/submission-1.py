class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for letter in s:
            if letter in pairs:
                if stack and stack[-1] == pairs[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)

        return True if not stack else False
                 
        