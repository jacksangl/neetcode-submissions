symbol = "#"
class Solution:
    
    def encode(self, strs: List[str]) -> str:

        res = ""

        for string in strs:
            length = str(len(string))
            res = res + length + symbol + string
            print(res)
        return res
    def decode(self, s: str) -> List[str]:
        cur = ""
        count = 0
        res = []
        length = ""
        while count < len(s):
            if s[count] == symbol:
                length = int(length)
                for i in range(count+1, count + 1 + length):
                    cur = cur + s[i]
                res.append(cur)
                
                cur = ""
                count = count + 1 + length
                length = ""
            else:
                length = length + s[count]
                count += 1
        return res