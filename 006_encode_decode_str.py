class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for s in strs:
            l = len(s)
            encodedStr += str(l) + '#' + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedList = []
        while (i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decodedList.append(s[j+1: j + 1 + length])
            i = j + 1 + length
            

        return decodedList 
