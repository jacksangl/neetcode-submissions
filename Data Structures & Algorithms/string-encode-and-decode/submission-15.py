class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = str(len(string))

            res += length + "#" + string
        print (res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        special = "#"
        i = 0
        while i < len(s):
            j = i
            while s[j] != special:
                j+= 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            print(s[j+1:j+1+length])

            i = j+1+length
        return res
