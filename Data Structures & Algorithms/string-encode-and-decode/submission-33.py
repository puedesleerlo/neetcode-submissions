class Solution:

    def encode(self, strs: List[str]) -> str:
        # print("&".join([]).split("&"))
        qr = ""
        for s in strs:
            nu = len(s)
            qr += f"#{nu}#{s}"
        return qr
    def decode(self, s: str) -> List[str]:
        rem = s
        def genn(rem):
            while len(rem) > 0:
                n = rem.find("#")
                rem = rem[n+1:]
                n2 = rem.find("#")
                N = rem[:n2]
                N = int(N)
                word = rem[n2+1:n2+N+1]
                rem = rem[n2+1+N:]
                yield word    
        return [val for val in genn(rem)]
