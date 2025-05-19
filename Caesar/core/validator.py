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
        return sum(word in self.dictionary for word in words) / max(len(words), 1)

    def validate_with_bert(self, sentence):
        words = sentence.split()
        total_score = 0
        valid_words = 0

        for i in range(len(words)):
            masked_words = words.copy()
            masked_words[i] = self.tokenizer.mask_token
            masked_sentence = " ".join(masked_words)

            inputs = self.tokenizer(masked_sentence, return_tensors="pt")
            mask_index = torch.where(inputs.input_ids == self.tokenizer.mask_token_id)[1]

            with torch.no_grad():
                outputs = self.model(**inputs)
            logits = outputs.logits

            predicted_token_id = torch.argmax(logits[0, mask_index, :], dim=-1).item()
            predicted_token = self.tokenizer.decode([predicted_token_id]).strip()

            if normalize_text(predicted_token.lower()) == normalize_text(words[i].lower()):
                total_score += 1
            valid_words += 1

        return total_score / valid_words if valid_words > 0 else 0

    def hybrid_validation(self, sentence):
        glc_score = 1 if self.validate_with_glc(sentence) else 0
        dict_score = self.validate_with_dict(sentence)
        bert_score = self.validate_with_bert(sentence)
        final_score = (glc_score * 0.3) + (dict_score * 0.3) + (bert_score * 0.3)
        return final_score, glc_score, dict_score, bert_score