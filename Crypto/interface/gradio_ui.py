import gradio as gr
from ciphers.caesar import auto_decrypt_caesar

def build_interface(dictionary):
    return gr.Interface(
        fn=lambda text: auto_decrypt_caesar(text, dictionary),
        inputs=gr.Textbox(label="Texto Criptografado (César)"),
        outputs=gr.Textbox(label="Texto Decriptografado"),
        title="🔓 Decriptador de Cifra de César (Português)",
        description="Digite um texto criptografado com Cifra de César para descriptografar automaticamente."
    )
