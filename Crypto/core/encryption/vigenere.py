from .base import EncryptionAlgorithm

class VigenereCipher(EncryptionAlgorithm):
    @property
    def name(self):
        return "Cifra de Vigenère"
    
    @property
    def description(self):
        return "Cifra polialfabética usando uma palavra-chave"
    
    def encrypt(self, text, key):
        # Implementação da cifra de Vigenère
        pass
    
    def decrypt(self, text, key):
        # Implementação da decifração
        pass
    
    def brute_force(self, text):
        # Implementação de ataque por análise de frequência
        pass