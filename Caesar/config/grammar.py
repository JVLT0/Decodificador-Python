from lark import Lark, Transformer

class SentenceValidator(Transformer):
    # Método chamado no início da análise da sentença
    def start(self, items):
        # Retorna verdadeiro se todos os itens (palavras, números, etc.) forem válidos de acordo com a gramática
        return all(items)

# Função para configurar a Gramática Livre de Contexto (GLC)
def setup_glc():
    # Define a gramática para validar sentenças
    grammar = """
    start: (word | number | punctuation | symbol | SPACE)+
    word: LETTER+
    number: DIGIT+
    punctuation: /[.,!?;:\\-—()“”"']/
    symbol: /[%@#$&*+=°ºª^~´]/
    SPACE: " "
    LETTER: /[a-zA-ZáéíóúâêôãõàèìòùäëïöüçñÁÉÍÓÚÂÊÔÃÕÀÈÌÒÙÄËÏÖÜÇÑ]/
    DIGIT: /[0-9]/
    %import common.WS
    %ignore WS
    """
    # Cria um objeto Lark com a gramática definida, usando o parser LALR e o transformer SentenceValidator
    return Lark(grammar, parser='lalr', transformer=SentenceValidator())