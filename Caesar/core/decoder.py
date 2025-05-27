import plotly.graph_objects as go
import gradio as gr
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.cipher import Cipher

# Classe responsável por decodificar o texto cifrado usando a cifra de César
class CaesarDecoder:
    # Inicializa o decodificador com um validador
    def __init__(self, validator):
        self.validator = validator

    # Método para avaliar um deslocamento específico na cifra de César
    def _evaluate_shift(self, text, shift):
        # Descriptografa o texto com o deslocamento fornecido
        decrypted = Cipher.caesar_decrypt(text, shift)
        # Calcula o score da Gramática Livre de Contexto (GLC)
        glc_score = 1 if self.validator.validate_with_glc(decrypted) else 0
        # Calcula o score do dicionário
        dict_score = self.validator.validate_with_dict(decrypted)
        # Calcula um score preliminar combinando GLC e dicionário
        prelim_score = (glc_score * 0.5) + (dict_score * 0.5)
        # Retorna o deslocamento, o texto descriptografado e os scores
        return shift, decrypted, prelim_score, glc_score, dict_score

    # Método principal para descriptografar o texto
    def decrypt(self, text):
        prelim_results = []

        # Utiliza ThreadPoolExecutor para avaliar múltiplos deslocamentos em paralelo
        with ThreadPoolExecutor() as executor:
            # Submete tarefas para avaliar cada deslocamento possível (1 a 25)
            futures = [executor.submit(self._evaluate_shift, text, shift) for shift in range(1, 26)]
            # Coleta os resultados à medida que as tarefas são concluídas
            for future in as_completed(futures):
                prelim_results.append(future.result())

        # Seleciona os 3 melhores candidatos com base no score preliminar
        top_candidates = sorted(prelim_results, key=lambda x: x[2], reverse=True)[:3]

        best_score = -1
        best_decryption = ""
        best_shift = 0
        all_scores = []

        # Itera sobre os melhores candidatos para avaliação final
        for shift, decrypted, _, glc_score, dict_score in top_candidates:
            # Calcula o score do BERT para avaliar a semântica do texto
            bert_score = self.validator.validate_with_bert(decrypted)
            # Calcula o score final ponderado
            final_score = (glc_score * 0.3) + (dict_score * 0.5) + (bert_score * 0.2)
            all_scores.append((shift, decrypted, final_score))

            # Atualiza o melhor resultado se o score atual for maior
            if final_score > best_score:
                best_score = final_score
                best_decryption = decrypted
                best_shift = shift
                best_bert_score = bert_score
                best_glc = glc_score
                best_dict = dict_score

        # Cria um gráfico de barras para visualizar os scores por deslocamento
        fig = go.Figure(data=[go.Bar(
            x=[s for s, _, _ in all_scores],
            y=[s for _, _, s in all_scores],
            marker=dict(color='#FF00FF')
        )])

        fig.update_layout(title="Scores por Shift", xaxis_title="Shift", yaxis_title="Score", height=400)

        # Formata o resultado para exibição
        resultado = f"📜 Texto decifrado:\n{best_decryption}\n\n🔁 Shift identificado: {best_shift}"

        # Formata a explicação detalhada dos scores
        explicacao = (
            f"🔍 **Componentes do score:**\n\n"
            f"**Estrutura (GLC):** {'✅ Válido' if best_glc else '❌ Inválido'}\n"
            f"**Léxico (Dicionário):** {best_dict:.2f}\n"
            f"**Semântica (BERT):** {best_bert_score:.2f}\n"
            f"⭐ **Score Final:** {best_score:.2f}"
        )

        # Retorna o resultado, a atualização da visibilidade da explicação e o gráfico
        return resultado, gr.update(visible=True), explicacao, fig