class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #brute force

        result = []

        def backtrack(path = "", openPar = 0, closedPar = 0):
            
            if openPar == closedPar == n:
                result.append(path)
                return
            if openPar < n:
                backtrack(path + "(", openPar+1, closedPar)
            if closedPar < openPar:
                backtrack(path + ")", openPar, closedPar+1)
        backtrack("", 0, 0)
        return result