from config.grammar import setup_glc                                
from config.settings import setup_bert, load_dictionary            
from core.validator import Validator                               
from core.decoder import CaesarDecoder                              
from interface.app import create_interface                          

# Função para inicializar todos os componentes necessários do sistema
def setup_system():
    # Configura o analisador de Gramática Livre de Contexto (GLC) para validação sintática
    parser = setup_glc()                                       
    # Carrega o tokenizer e o modelo BERT para análise semântica
    tokenizer, model = setup_bert()                                
    # Carrega o dicionário de palavras para validação lexical
    dictionary = load_dictionary()                                 
    # Cria um validador que utiliza GLC, BERT e dicionário
    validator = Validator(parser, tokenizer, model, dictionary)    
    # Cria o decodificador de César, que utiliza o validador para avaliar as tentativas de decodificação
    decoder = CaesarDecoder(validator)                             
    return decoder

# Bloco de execução principal: inicia o sistema e a interface se o script for executado diretamente
if __name__ == "__main__":
    # Inicializa o sistema de descriptografia
    decoder = setup_system()                                        
    # Cria a interface do usuário usando Gradio
    interface = create_interface(decoder)                          
    # Inicia a aplicação web da interface
    interface.launch()                                            