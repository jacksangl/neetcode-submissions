class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = collections.deque()
        chars = {'}': '{', ']': '[', ')': '('}

        
        for letter in s:
            if letter in chars.values():
                stack.append(letter)
            else:
                if letter in chars and len(stack) > 0 and chars[letter] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack

