class Solution:

    def encode(self, strs: List[str]) -> str:
        s= ""
        for i in strs:
            s+= str(len(i)) + "#" + i
        return s
            

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while(s[j] != "#"):
                j+=1
            
            lens = int(s[i:j])
            d = ""
            
            d = s[j+1:j+1+lens]

            result.append(d)
            i = lens+1+j
        return result

