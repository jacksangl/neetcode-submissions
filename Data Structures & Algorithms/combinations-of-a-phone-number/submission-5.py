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
            for ch in bank[int(digits[i])]:
                backtrack(i + 1, sol + ch)
        backtrack(0, "")
        return res


            




