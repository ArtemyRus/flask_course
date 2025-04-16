import sys

def decrypt(encryption: str) -> str:
    result = []
    i = 0
    while i < len(encryption):
        if encryption[i] == '.':
            if i + 1 < len(encryption) and encryption[i + 1] == '.':
                if len(result) > 0:
                    result.pop()
                i += 2
            else: i += 1
        else:
            result.append(encryption[i])
            i += 1
    return ''.join(result)


if __name__ == '__main__':
    data: str = sys.stdin.read().strip()
    decryption: str = decrypt(data)
    print(decryption)