class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        bank = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
            }
        def backtrack(i, sol):
            if i == len(digits):
                if len(sol) > 0: res.append(sol[:])
                return
            backtrack(i+1, sol + bank[int(digits[i])][0])
            backtrack(i+1, sol + bank[int(digits[i])][1])
            backtrack(i+1, sol + bank[int(digits[i])][2])
            if int(digits[i]) == 7 or int(digits[i]) == 9: backtrack(i+1, sol + bank[int(digits[i])][3])
        backtrack(0, "")
        return res


            




