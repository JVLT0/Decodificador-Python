from config.grammar import setup_glc
from config.settings import setup_bert, load_dictionary
from core.validator import Validator
from core.decoder import CaesarDecoder
from interface.app import create_interface

def setup_system():
    parser = setup_glc()
    tokenizer, model = setup_bert()
    dictionary = load_dictionary()
    validator = Validator(parser, tokenizer, model, dictionary)
    decoder = CaesarDecoder(validator)
    return decoder

if __name__ == "__main__":
    decoder = setup_system()
    interface = create_interface(decoder)
    interface.launch()