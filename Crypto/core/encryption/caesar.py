from .base import BaseCipher

class CaesarCipher(BaseCipher):
    def decrypt(self, text: str, shift: int) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                result.append(chr((ord(char) - base - shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)