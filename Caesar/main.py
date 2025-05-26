# Importa os módulos de configuração e lógica do sistema
from config.grammar import setup_glc                                # GLC para validação sintática
from config.settings import setup_bert, load_dictionary             # BERT e dicionário
from core.validator import Validator                                # Classe de validação
from core.decoder import CaesarDecoder                              # Decodificador de César
from interface.app import create_interface                          # Interface Gradio

# Inicializa todos os componentes necessários
def setup_system():
    parser = setup_glc()                                            # GLC
    tokenizer, model = setup_bert()                                 # Modelo BERT
    dictionary = load_dictionary()                                  # Dicionário de palavras
    validator = Validator(parser, tokenizer, model, dictionary)     # Monta validador
    decoder = CaesarDecoder(validator)                              # Decodificador principal
    return decoder

# Executa a interface se chamado diretamente
if __name__ == "__main__":
    decoder = setup_system()                                        # Inicializa o sistema
    interface = create_interface(decoder)                           # Cria interface
    interface.launch()                                              # Inicia app web
