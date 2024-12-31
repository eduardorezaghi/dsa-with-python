# Leetcode: 271. Encode and Decode Strings

class Codec:
    def encode(self, strs: list[str]) -> str:
        encoded = [ f'{len(s)}/{s}' for s in strs ]
        return ' '.join(encoded)


    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        while i < len(s):
            slash = s.index('/', i)
            size = int(s[i:slash])
            decoded.append(s[slash+1:slash+1+size])
            i = slash + 1 + size

        print(decoded)
        return decoded

if __name__ == '__main__':
    # Arrange
    strs = ["leet", "code", "is", "awful"]
    codec = Codec()

    # Act
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)

    # Assert
    assert strs == decoded
    print('All tests passed')