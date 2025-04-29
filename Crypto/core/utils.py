import unicodedata
import re

def preprocess_text(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f if word.strip())

def count_valid_words(text, dictionary):
    words = [w for w in text.split()]
    return sum(1 for word in words if word in dictionary)