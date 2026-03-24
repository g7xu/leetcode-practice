class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        
        for s in strs:
            res += str(len(s)) + "*" + s

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        p = 0
        res = []
        while p < len(s):
            num = ""
            while s[p] != "*":
                num += s[p]
                p += 1

            num = int(num)
            p += 1

            res.append(s[p: p + num])
            p += num

        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))