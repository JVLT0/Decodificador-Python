import gradio as gr
from core.decryption import decrypt_caesar

def launch_interface():
    with gr.Blocks() as interface:
        gr.Markdown("# \U0001F9E0 Decriptador Híbrido de César")
        gr.Markdown("GLC + BERT + Dicionário + Correções Inteligentes com Dashboard Interativo")

        input_text = gr.Textbox(label="Texto Cifrado", lines=2)
        output_text = gr.Textbox(label="Resultado", lines=7)

        with gr.Accordion("\U0001F4CA Dashboard de Validação", open=False):
            line_plot = gr.Plot(label="Pontuação por Shift")
            pie_plot = gr.Plot(label="Distribuição de Confiança")

        decrypt_btn = gr.Button("\U0001F513 Decriptar")

        decrypt_btn.click(fn=decrypt_caesar, inputs=[input_text], outputs=[output_text, line_plot, pie_plot])

    interface.launch()