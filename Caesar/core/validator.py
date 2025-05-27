import re
import torch
from utils.text_utils import normalize_text

# Classe para validar a qualidade do texto descriptografado
class Validator:
    # Inicializa o validador com o parser GLC, tokenizer BERT, modelo BERT e dicionário
    def __init__(self, parser, tokenizer, model, dictionary):
        self.parser = parser
        self.tokenizer = tokenizer
        self.model = model
        self.dictionary = dictionary

    # Método para validar a estrutura da sentença usando a Gramática Livre de Contexto (GLC)
    def validate_with_glc(self, sentence):
        try:
            # Tenta analisar a sentença com o parser GLC
            self.parser.parse(sentence)
            return True
        except:
            # Retorna Falso se a análise falhar (sentença inválida)
            return False

    # Método para validar o uso de palavras do dicionário na sentença
    def validate_with_dict(self, sentence):
        # Extrai as palavras da sentença, normalizando o texto
        words = re.findall(r'\b\w+\b', normalize_text(sentence.lower()))
        # Retorna 0.0 se não houver palavras
        if not words:
            return 0.0
        # Conta quantas palavras da sentença estão presentes no dicionário
        valid_words = sum(word in self.dictionary for word in words)
        # Retorna a proporção de palavras válidas
        return valid_words / len(words)

    # Método para validar a semântica da sentença usando o modelo BERT
    def validate_with_bert(self, text, max_words=5):
        # Seleciona as primeiras max_words palavras para avaliar (comprimento mínimo de 3 caracteres)
        words = [w for w in text.split() if len(w) >= 3][:max_words]
        correct = 0
        for word in words:
            try:
                # Mascara a palavra atual no texto
                masked = text.replace(word, self.tokenizer.mask_token, 1)
                # Tokeniza o texto mascarado
                inputs = self.tokenizer(masked, return_tensors="pt", truncation=True, max_length=512)
                # Faz a predição da palavra mascarada usando o modelo BERT
                with torch.no_grad():
                    outputs = self.model(**inputs)
                pred = self.tokenizer.decode(outputs.logits[0, torch.where(inputs.input_ids == self.tokenizer.mask_token_id)[1]].argmax(-1)).strip()
                # Incrementa o contador se a predição for igual à palavra original
                if normalize_text(pred.lower()) == normalize_text(word.lower()):
                    correct += 1
            except:
                continue
        # Retorna a precisão das predições
        return correct / len(words) if words else 0.0