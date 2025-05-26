import gradio as gr

def create_interface(decoder):
    with gr.Blocks() as interface:
        gr.Markdown("# 🔓 Decriptador de César")

        with gr.Row():
            input_text = gr.Textbox(label="🔐 Texto Cifrado", lines=2)
            output_text = gr.Textbox(label="📜 Resultado", lines=6)

        with gr.Accordion("📊 Detalhes Técnicos", open=False):
            explanation_text = gr.Markdown(visible=False)
            plot_output = gr.Plot(container=True)

        btn = gr.Button("Descriptografar")
        btn.click(fn=decoder.decrypt, inputs=[input_text], outputs=[output_text, explanation_text, explanation_text, plot_output])

    return interface