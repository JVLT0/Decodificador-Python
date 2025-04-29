from core.utils import preprocess_text, count_valid_words
from core.parser import parser
from lark.exceptions import UnexpectedInput

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def auto_decrypt_caesar(text, dictionary):
    text = preprocess_text(text.lower())

    best_shift = None
    best_text = ""
    best_valid_count = -1
    failed_shifts = []

    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(text, shift)

        try:
            parser.parse(decrypted_text)
        except UnexpectedInput:
            failed_shifts.append((shift, decrypted_text))
            continue

        valid_count = count_valid_words(decrypted_text, dictionary)

        if valid_count > best_valid_count:
            best_valid_count = valid_count
            best_shift = shift
            best_text = decrypted_text

    if best_valid_count > 0:
        result = f"Texto descriptografado: {best_text} (Shift usado: {best_shift})"
    else:
        result = "Não foi possível descriptografar o texto."

    error_report = "\n\n--- Tentativas rejeitadas pelo parser ---\n"
    for shift, txt in failed_shifts[:5]:
        error_report += f"[Shift {shift}] → {txt}\n"

    return result + error_report