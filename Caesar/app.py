import gradio as gr
import re
import unicodedata
from lark import Lark, Transformer
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

# ====================== CONFIGURAÇÃO GLC ======================
grammar = """
start: sentence
sentence: (word | punctuation)+
word: LETTER+
punctuation: /[.,!?;:]/
LETTER: /[a-zA-ZáéíóúâêôãõàèìòùäëïöüçñÁÉÍÓÚÂÊÔÃÕÀÈÌÒÙÄËÏÖÜÇÑ]/
"""

class SentenceValidator(Transformer):
    def sentence(self, items):
        return all(items)

parser = Lark(grammar, parser='lalr', transformer=SentenceValidator())

# ====================== CONFIGURAÇÃO BERT ======================
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")

# ====================== DICIONÁRIO ======================
with open("portuguese_words.txt", "r", encoding="utf-8") as f:
    DICTIONARY = set(word.strip().lower() for word in f.readlines())

# ====================== FUNÇÕES PRINCIPAIS ======================
def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def validate_with_glc(sentence):
    try:
        parser.parse(sentence)
        return True
    except:
        return False

def validate_with_bert(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    return torch.softmax(logits, dim=-1).mean().item()

def validate_with_dict(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return sum(word in DICTIONARY for word in words) / max(len(words), 1)

def hybrid_validation(sentence):
    # Peso 1: Validação estrutural (GLC)
    glc_score = 1 if validate_with_glc(sentence) else 0
    
    # Peso 2: Validação semântica (BERT)
    bert_score = validate_with_bert(sentence)
    
    # Peso 3: Validação léxica (Dicionário)
    dict_score = validate_with_dict(sentence)
    
    return (glc_score * 0.4) + (bert_score * 0.3) + (dict_score * 0.3)

# ====================== INTERFACE ======================
def decrypt_caesar(text):
    best_score = -1
    best_decryption = ""
    best_shift = 0
    
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        score = hybrid_validation(decrypted)
        
        if score > best_score:
            best_score = score
            best_decryption = decrypted
            best_shift = shift
    
    return f"{best_decryption}\n\nShift: {best_shift}\nScore: {best_score:.2f}"

interface = gr.Interface(
    fn=decrypt_caesar,
    inputs=gr.Textbox(label="Texto Cifrado"),
    outputs=gr.Textbox(label="Resultado"),
    title="Decriptador Híbrido de César",
    description="Combina GLC, autômatos e BERT para descriptografia inteligente"
)

if __name__ == "__main__":
    interface.launch()