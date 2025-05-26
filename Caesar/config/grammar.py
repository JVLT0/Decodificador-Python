from lark import Lark, Transformer

class SentenceValidator(Transformer):
    def start(self, items):
        return all(items)

def setup_glc():
    # Define uma gramática simples para validar sentenças
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
    return Lark(grammar, parser='lalr', transformer=SentenceValidator())
