from transformers import AutoTokenizer, AutoModelForMaskedLM
import unicodedata

# Função para configurar o tokenizer e o modelo BERT
def setup_bert():
    # Carrega o tokenizer pré-treinado do BERT para a versão multilingue com case sensitive
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    # Carrega o modelo pré-treinado do BERT para a tarefa de Masked Language Modeling
    model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")
    return tokenizer, model

# Função para carregar o dicionário de palavras em português
def load_dictionary():
    # Abre o arquivo contendo as palavras em português
    with open("assets/portuguese_words.txt", "r", encoding="utf-8") as f:
        # Lê cada palavra, normaliza (remove acentos), converte para minúsculo e armazena em um conjunto
        return set(unicodedata.normalize("NFKD", word.strip().lower()).encode("ASCII", "ignore").decode("ASCII") for word in f)