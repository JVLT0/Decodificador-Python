from lark import Lark

simple_grammar = """
    start: WORD (WORD)*

    %import common.WORD
    %import common.WS
    %ignore WS
"""

parser = Lark(simple_grammar, start='start', parser='earley')