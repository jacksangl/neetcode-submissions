class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", "-", "*", "/"}
        for num in tokens:

            if num in symbols:    
                num1, num2 = stack.pop(), stack.pop()
                if num == "+":
                    stack.append(num1 + num2)
                elif num == "-":
                    stack.append(num2-num1)
                elif num == "/" and num2 != 0:
                    stack.append(int(num2/num1))
                
                else:
                    stack.append(num1*num2)
            else:
                num = int(num)
                stack.append(num)
        return stack.pop()