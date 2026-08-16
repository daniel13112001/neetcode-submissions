class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('-')
            encoded.append(s)

        encoded = "".join(encoded)

        return encoded

            

    #5-hello-5-world

    def decode(self, s: str) -> List[str]:

        i = 0

        length = []
        decoded = []

        while i < len(s):
            if s[i] != '-':
                length.append(str(s[i]))
                i += 1
                continue

            count = int("".join(length))
            cur = []

            for j in range(i+1, i+count+1):
                cur.append(s[j])

            decoded.append("".join(cur))

            i += count + 1
            length = []
            
        return decoded
            
        

        
    
