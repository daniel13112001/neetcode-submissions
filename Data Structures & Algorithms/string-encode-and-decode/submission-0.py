class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = []

        for s in strs:
            encoded_strs.append(str(len(s)))
            encoded_strs.append("#")
            encoded_strs.append(s)

        return "".join(encoded_strs)
    

    def decode(self, s: str) -> List[str]:

        decoded_strs = []

        i = 0
        j = 0 # This will always be pointing to the start of a number

        while i < len(s):
            while s[j] != "#":
                j += 1
            print(i,j)
            str_len = int(s[i:j])
            print(s[j+1:j+str_len+1])
            decoded_strs.append(s[j+1:j+str_len+1])
            i = j + str_len + 1
            j = i

        return decoded_strs




        
