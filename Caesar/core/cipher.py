class Cipher:
    @staticmethod
    def caesar_decrypt(text, shift):
        decrypted = ""
        for char in text:
            if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz":
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                decrypted += char
        return decrypted