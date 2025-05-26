import plotly.graph_objects as go
import gradio as gr
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.cipher import Cipher

class CaesarDecoder:
    def __init__(self, validator):
        self.validator = validator

    def _evaluate_shift(self, text, shift):
        decrypted = Cipher.caesar_decrypt(text, shift)
        # Avalia com GLC e Dicionário
        glc_score = 1 if self.validator.validate_with_glc(decrypted) else 0
        dict_score = self.validator.validate_with_dict(decrypted)
        prelim_score = (glc_score * 0.5) + (dict_score * 0.5)
        return shift, decrypted, prelim_score, glc_score, dict_score

    def decrypt(self, text):
        prelim_results = []

        # Avalia todos os 25 shifts possíveis
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._evaluate_shift, text, shift) for shift in range(1, 26)]
            for future in as_completed(futures):
                prelim_results.append(future.result())

        # Seleciona os 3 melhores resultados preliminares
        top_candidates = sorted(prelim_results, key=lambda x: x[2], reverse=True)[:3]

        best_score = -1
        best_decryption = ""
        best_shift = 0
        all_scores = []

        for shift, decrypted, _, glc_score, dict_score in top_candidates:
            bert_score = self.validator.validate_with_bert(decrypted)
            final_score = (glc_score * 0.3) + (dict_score * 0.5) + (bert_score * 0.2)
            all_scores.append((shift, decrypted, final_score))

            if final_score > best_score:
                best_score = final_score
                best_decryption = decrypted
                best_shift = shift

        # Gera gráfico de barras
        fig = go.Figure(data=[go.Bar(
            x=[s for s, _, _ in all_scores],
            y=[s for _, _, s in all_scores],
            marker=dict(color='#FF00FF')
        )])

        fig.update_layout(title="Scores por Shift", xaxis_title="Shift", yaxis_title="Score", height=400)

        # Resultado textual e explicação
        resultado = f"📜 Texto decifrado:\n{best_decryption}\n\n🔁 Shift identificado: {best_shift}"
        explicacao = f"**GLC:** {glc_score}, **Dicionário:** {dict_score}, **BERT:** {bert_score}, **Final:** {best_score}"

        return resultado, gr.update(visible=True), explicacao, fig