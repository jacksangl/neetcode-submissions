class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element.isnumeric() or len(element) > 1:
                stack.append(int(element))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if element == "+":
                stack.append(num1 + num2)
            elif element == "-":
                stack.append(num1 - num2)
            elif element == "*":
                stack.append(num1 * num2)
            else:
                stack.append(int(num1/ num2))
        return stack[0]
