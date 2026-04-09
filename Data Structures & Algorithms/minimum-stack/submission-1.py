class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)
    def pop(self) -> None:
        res = self.stack.pop()

        if res == self.mins[-1]: self.mins.pop()
        return res
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
class ListNode:
    def __init__(self, val: int):
        self.val = 0
        self.left = None
        self.right = None
        
