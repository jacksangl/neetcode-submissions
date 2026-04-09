class Solution:

    def encode(self, strs: List[str]) -> str:
        words = ""
        for string in strs:
            word = ""
            length = len(string)
            word+= str(length)
            word+= "#"
            word+= string
            words+= word
        return words

    def decode(self, s: str) -> List[str]:
        length = 0
        strings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            strings.append(str(s[j+1: j + 1 + length]))
            i = j + length + 1
                
        return strings