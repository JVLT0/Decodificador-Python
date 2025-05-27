class Cipher:
    # Método estático para descriptografar um texto usando a cifra de César
    @staticmethod
    def caesar_decrypt(text, shift):
        # Inicializa a string que armazenará o texto descriptografado
        decrypted = ""
        # Itera por cada caractere no texto cifrado
        for char in text:
            # Verifica se o caractere é uma letra do alfabeto
            if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz":
                # Determina o offset ASCII para maiúsculas ou minúsculas
                ascii_offset = ord('A') if char.isupper() else ord('a')
                # Aplica o deslocamento de César inverso
                decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                # Mantém caracteres não alfabéticos inalterados
                decrypted += char
        return decrypted