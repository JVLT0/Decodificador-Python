import re
from lark import Lark, Transformer
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

with open("data/portuguese_words.txt", "r", encoding="utf-8") as f:
    DICTIONARY = set(word.strip().lower() for word in f.readlines())

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
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")

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
    glc_score = 1 if validate_with_glc(sentence) else 0
    bert_score = validate_with_bert(sentence)
    dict_score = validate_with_dict(sentence)
    return (glc_score * 0.4) + (bert_score * 0.3) + (dict_score * 0.3), glc_score, bert_score, dict_score