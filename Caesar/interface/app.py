import gradio as gr

# Função para criar a interface do usuário com Gradio
def create_interface(decoder):
    # Cria os blocos da interface
    with gr.Blocks() as interface:
        # Adiciona um título à interface
        gr.Markdown("# 🔓 Decodificador de Criptografia")

        # Cria uma linha para os campos de entrada e saída
        with gr.Row():
            # Campo de entrada para o texto cifrado
            input_text = gr.Textbox(label="🔐 Texto Cifrado", lines=2)
            # Campo de saída para o texto descriptografado
            output_text = gr.Textbox(label="📜 Resultado", lines=6)

        # Cria um acordeão para exibir detalhes técnicos
        with gr.Accordion("📊 Detalhes Técnicos", open=False):
            # Campo para exibir a explicação dos scores
            explanation_text = gr.Markdown(visible=False)
            # Campo para exibir o gráfico de scores por shift
            plot_output = gr.Plot(container=True)

        # Cria um botão para iniciar a descriptografia
        btn = gr.Button("Descriptografar")
        # Define a ação do botão para chamar o método decrypt do decodificador
        btn.click(fn=decoder.decrypt, inputs=[input_text], outputs=[output_text, explanation_text, explanation_text, plot_output])

    return interface