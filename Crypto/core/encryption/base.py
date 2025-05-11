from abc import ABC, abstractmethod

class BaseCipher(ABC):
    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass