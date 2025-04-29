from core.utils import load_dictionary
from interface.gradio_ui import build_interface

if __name__ == "__main__":
    portuguese_words = load_dictionary("data/portuguese_words.txt")
    iface = build_interface(portuguese_words)
    iface.launch()
