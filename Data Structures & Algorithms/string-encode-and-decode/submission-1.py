class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = "" + chr(len(strs))
        message = ""
        for i in strs:
            encode += chr(len(i))
            message += i
        return encode + message

    def decode(self, s: str) -> List[str]:
        length = ord(s[0])
        decode = ["" for i in range(length)]
        p1 = 1
        p2 = length + 1
        for i in range(length):
            for j in range(ord(s[p1])):
                decode[p1 - 1] += s[p2]
                p2 += 1
            p1 += 1
        
        return decode