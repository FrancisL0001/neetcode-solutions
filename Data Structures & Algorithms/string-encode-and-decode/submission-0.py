class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '.' + s
        return res


    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        buf = ''
        while i < len(s):
            if s[i] == '.':
                str_len = int(buf) 
                i+=1
                res.append(s[i:i+str_len])
                i+=str_len
                buf = ''
            else:
                buf += s[i]
                i += 1
        return res

