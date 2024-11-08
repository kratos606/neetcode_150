class Solution:
    def __init__(self):
        self.rot13_table = str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        )

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            rot13_s = s.translate(self.rot13_table)
            encoded.append(f"{len(rot13_s)}#{rot13_s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            rot13_s = s[i:i + length]
            decoded.append(rot13_s.translate(self.rot13_table))
            i += length
        return decoded
