import unicodedata

def normalize_text(text):
    # Remove acentos e normaliza caracteres especiais
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )