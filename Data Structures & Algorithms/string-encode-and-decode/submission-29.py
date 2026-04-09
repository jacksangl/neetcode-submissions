class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        parts = []
        for string in strs:
            parts.append(str(len(string)))
            parts.append("#")
            parts.append(string)
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []
        while ptr < len(s):
            # find length
            length = 0
            while ptr < len(s) and s[ptr] != '#':
                length *= 10
                length += int(s[ptr])
                ptr += 1
            res.append(s[ptr+1:ptr+1+length])
            ptr = length + ptr + 1
        
        return res