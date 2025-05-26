import plotly.graph_objects as go
import gradio as gr
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.cipher import Cipher

class CaesarDecoder:
    def __init__(self, validator):
        self.validator = validator

    def _evaluate_shift(self, text, shift):
        decrypted = Cipher.caesar_decrypt(text, shift)
        # Fase 1: GLC e Dicionário apenas
        glc_score = 1 if self.validator.validate_with_glc(decrypted) else 0
        dict_score = self.validator.validate_with_dict(decrypted)
        prelim_score = (glc_score * 0.5) + (dict_score * 0.5)
        return shift, decrypted, prelim_score, glc_score, dict_score

    def decrypt(self, text):
        prelim_results = []

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._evaluate_shift, text, shift) for shift in range(1, 26)]
            for future in as_completed(futures):
                prelim_results.append(future.result())

        # Selecionar top 3 shifts preliminarmente
        top_candidates = sorted(prelim_results, key=lambda x: x[2], reverse=True)[:3]

        best_score = -1
        best_decryption = ""
        best_shift = 0
        all_scores = []

        for shift, decrypted, prelim_score, glc_score, dict_score in top_candidates:
            bert_score = self.validator.validate_with_bert(decrypted, max_words=5)
            final_score = (glc_score * 0.3) + (dict_score * 0.5) + (bert_score * 0.2)
            all_scores.append((shift, decrypted, final_score))

            if final_score > best_score:
                best_score = final_score
                best_decryption = decrypted
                best_shift = shift
                best_bert_score = bert_score
                best_glc = glc_score
                best_dict = dict_score

        shifts = [s for s, _, _ in all_scores]
        scores = [s for _, _, s in all_scores]
        fig = go.Figure(data=[go.Bar(x=shifts, y=scores)])
        fig.update_layout(title="Scores por Shift", xaxis_title="Shift", yaxis_title="Score")

        explanation = (
            f"🔍 **Componentes do score:**\n"
            f" - Estrutura (GLC): {'✅ Válido' if best_glc else '❌ Inválido'}\n"
            f" - Léxico (Dicionário): {best_dict:.2f}\n"
            f" - Semântica (BERT): {best_bert_score:.2f}\n"
            f" - ⭐ Score Final: {best_score:.2f}"
        )

        resultado = f"📜 Texto decifrado:\n{best_decryption}\n\n🔁 Shift identificado: {best_shift}"
        return resultado, gr.update(visible=True), explanation, fig
