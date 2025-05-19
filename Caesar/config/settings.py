from transformers import AutoTokenizer, AutoModelForMaskedLM
import unicodedata

def setup_bert():
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")
    return tokenizer, model

def load_dictionary():
    with open("assets/portuguese_words.txt", "r", encoding="utf-8") as f:
        return set(unicodedata.normalize("NFKD", word.strip().lower()).encode("ASCII", "ignore").decode("ASCII") for word in f)