import plotly.graph_objects as go
import gradio as gr
from core.cipher import Cipher

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