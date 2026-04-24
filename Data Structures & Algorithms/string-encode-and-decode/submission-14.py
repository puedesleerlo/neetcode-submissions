class Solution:

    def encode(self, strs: List[str]) -> str:
        # print("&".join([]).split("&"))
        qr = ""
        for s in strs:
            nu = len(s)
            qr += f"<len={nu}=len>{s}"
        return qr
    def decode(self, s: str) -> List[str]:
        ho = s.split("<len=")
        stt = []
        print(s, ho)
        for h in ho:
            sep = h.split("=len>")
            print(sep)
            if len(sep) > 1 and int(sep[0]) == len(sep[1]):
                stt.append(sep[1])
        return stt
