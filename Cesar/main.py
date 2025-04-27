from lark import Lark
from lark.exceptions import UnexpectedInput
import gradio as gr
import unicodedata
import re

# --- Funções de apoio ---

def preprocess_text(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')  # Remove acentos
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Mantém apenas letras e espaços
    return text

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f if word.strip())

def count_valid_words(text, dictionary):
    words = [w for w in text.split()]
    return sum(1 for word in words if word in dictionary)

# --- Gramática super simples só para validar palavras separadas ---

simple_grammar = """
    start: WORD (WORD)*

    %import common.WORD
    %import common.WS
    %ignore WS
"""

parser = Lark(simple_grammar, start='start', parser='earley')

# --- Funções principais ---

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def auto_decrypt_caesar(text):
    text = preprocess_text(text.lower())

    best_shift = None
    best_text = ""
    best_valid_count = -1

    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(text, shift)

        try:
            parser.parse(decrypted_text)  # Tenta validar separação de palavras
        except UnexpectedInput:
            continue

        valid_count = count_valid_words(decrypted_text, portuguese_words)

        if valid_count > best_valid_count:
            best_valid_count = valid_count
            best_shift = shift
            best_text = decrypted_text

    if best_valid_count > 0:
        return f"Texto descriptografado: {best_text} (Shift usado: {best_shift})"
    else:
        return "Não foi possível descriptografar o texto."

# --- Interface Gradio ---

iface = gr.Interface(
    fn=auto_decrypt_caesar,
    inputs=gr.Textbox(label="Texto Criptografado (César)"),
    outputs=gr.Textbox(label="Texto Decriptografado"),
    title="🔓 Decriptador de Cifra de César (Português)",
    description="Digite um texto criptografado com Cifra de César para descriptografar automaticamente."
)

# --- Execução ---

if __name__ == "__main__":
    portuguese_words = load_dictionary('portuguese_words.txt')
    iface.launch()
