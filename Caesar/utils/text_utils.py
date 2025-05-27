import unicodedata

# Função para normalizar o texto removendo acentos e caracteres especiais
def normalize_text(text):
    # Utiliza a normalização NFD para separar caracteres acentuados
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        # Filtra os caracteres que são marcas diacríticas (acentos)
        if unicodedata.category(c) != 'Mn'
    )