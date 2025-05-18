import gradio as gr
import re
import unicodedata
from lark import Lark, Transformer
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch
import plotly.graph_objects as go

# ====================== MÓDULO DE CONFIGURAÇÃO ======================
class Config:
    @staticmethod
    def setup_glc():
        grammar = """
        start: (word | number | punctuation | symbol | SPACE)+
        word: LETTER+
        number: DIGIT+
        punctuation: /[.,!?;:\\-—()“”"']/
        symbol: /[%@#$&*+=°ºª^~´]/
        SPACE: " "
        LETTER: /[a-zA-ZáéíóúâêôãõàèìòùäëïöüçñÁÉÍÓÚÂÊÔÃÕÀÈÌÒÙÄËÏÖÜÇÑ]/
        DIGIT: /[0-9]/
        %import common.WS
        %ignore WS
        """
        class SentenceValidator(Transformer):
            def start(self, items):
                return all(items)
        return Lark(grammar, parser='lalr', transformer=SentenceValidator())

    @staticmethod
    def setup_bert():
        tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
        model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")
        return tokenizer, model

    @staticmethod
    def load_dictionary():
        with open("portuguese_words.txt", "r", encoding="utf-8") as f:
            return set(unicodedata.normalize("NFKD", word.strip().lower()).encode("ASCII", "ignore").decode("ASCII") for word in f)

# ====================== MÓDULO DE UTILIDADES ======================
class TextUtils:
    @staticmethod
    def normalize_text(text):
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )

# ====================== MÓDULO DE CRIPTOGRAFIA ======================
class Cipher:
    @staticmethod
    def caesar_decrypt(text, shift):
        decrypted = ""
        for char in text:
            if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz":
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                decrypted += char
        return decrypted

# ====================== MÓDULO DE VALIDAÇÃO ======================
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
        words = re.findall(r'\b\w+\b', TextUtils.normalize_text(sentence.lower()))
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

            if TextUtils.normalize_text(predicted_token.lower()) == TextUtils.normalize_text(words[i].lower()):
                total_score += 1
            valid_words += 1

        return total_score / valid_words if valid_words > 0 else 0

    def hybrid_validation(self, sentence):
        glc_score = 1 if self.validate_with_glc(sentence) else 0
        dict_score = self.validate_with_dict(sentence)
        bert_score = self.validate_with_bert(sentence)
        final_score = (glc_score * 0.3) + (dict_score * 0.3) + (bert_score * 0.3)
        return final_score, glc_score, dict_score, bert_score

# ====================== MÓDULO PRINCIPAL ======================
class CaesarDecoder:
    def __init__(self, validator):
        self.validator = validator

    def decrypt(self, text):
        best_score = -1
        best_decryption = ""
        best_shift = 0
        all_scores = []

        for shift in range(1, 26):
            decrypted = Cipher.caesar_decrypt(text, shift)
            score, *_ = self.validator.hybrid_validation(decrypted)
            all_scores.append((shift, decrypted, score))

            if score > best_score:
                best_score = score
                best_decryption = decrypted
                best_shift = shift

        shifts = [s for s, _, _ in all_scores]
        scores = [s for _, _, s in all_scores]
        fig = go.Figure(data=[go.Bar(x=shifts, y=scores)])
        fig.update_layout(title="Scores por Shift", xaxis_title="Shift", yaxis_title="Score")

        final_score, glc_score, dict_score, bert_score = self.validator.hybrid_validation(best_decryption)
        explanation = (
            f"🔍 **Componentes do score:**\n"
            f" - Estrutura (GLC): {'✅ Válido' if glc_score else '❌ Inválido'}\n"
            f" - Léxico (Dicionário): {dict_score:.2f}\n"
            f" - Semântica (BERT): {bert_score:.2f}\n"
            f" - ⭐ Score Final: {final_score:.2f}"
        )

        resultado = f"📜 Texto decifrado:\n{best_decryption}\n\n🔁 Shift identificado: {best_shift}"
        return resultado, gr.update(visible=True), explanation, fig

# ====================== INICIALIZAÇÃO ======================
def setup_system():
    parser = Config.setup_glc()
    tokenizer, model = Config.setup_bert()
    dictionary = Config.load_dictionary()
    validator = Validator(parser, tokenizer, model, dictionary)
    decoder = CaesarDecoder(validator)
    return decoder

# ====================== INTERFACE ======================
def create_interface(decoder):
    with gr.Blocks() as interface:
        gr.Markdown("# 🔓 Decriptador Híbrido de César")
        gr.Markdown("Combina GLC, Dicionário e BERT para validar e descriptografar mensagens.")

        with gr.Row():
            input_text = gr.Textbox(label="🔐 Texto Cifrado", lines=2)
            output_text = gr.Textbox(label="📜 Resultado", lines=6)

        with gr.Accordion("📊 Detalhes Técnicos", open=False):
            explanation_text = gr.Markdown(visible=False)
            plot_output = gr.Plot()

        btn = gr.Button("Descriptografar")
        btn.click(fn=decoder.decrypt, inputs=[input_text], outputs=[output_text, explanation_text, explanation_text, plot_output])

    return interface

if __name__ == "__main__":
    decoder = setup_system()
    interface = create_interface(decoder)
    interface.launch()