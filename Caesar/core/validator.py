import re
import torch
from utils.text_utils import normalize_text

class Validator:
    def __init__(self, parser, tokenizer, model, dictionary):
        self.parser = parser
        self.tokenizer = tokenizer
        self.model = model
        self.dictionary = dictionary

    def validate_with_glc(self, sentence):
        try:
            self.parser.parse(sentence)
            return True
        except:
            return False

    def validate_with_dict(self, sentence):
        words = re.findall(r'\b\w+\b', normalize_text(sentence.lower()))
        if not words:
            return 0.0
        valid_words = sum(word in self.dictionary for word in words)
        return valid_words / len(words)

    def validate_with_bert(self, text, max_words=5):
        # Avaliação semântica com BERT usando até 5 palavras mascaradas
        words = [w for w in text.split() if len(w) >= 3][:max_words]
        correct = 0
        for word in words:
            try:
                masked = text.replace(word, self.tokenizer.mask_token, 1)
                inputs = self.tokenizer(masked, return_tensors="pt", truncation=True, max_length=512)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                pred = self.tokenizer.decode(outputs.logits[0, torch.where(inputs.input_ids == self.tokenizer.mask_token_id)[1]].argmax(-1)).strip()
                if normalize_text(pred.lower()) == normalize_text(word.lower()):
                    correct += 1
            except:
                continue
        return correct / len(words) if words else 0.0
