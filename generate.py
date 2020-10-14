from nltk import CFG
from nltk import ChartParser # parse_cfg, ChartParser
from random import choice
import re

def resolve_grammar(G):
    def file_contents(s):
        filename = f"name-segments/{s.group(1)}"
        try:
            terms = open(filename).readlines()
            s = ""
            for i, t in enumerate(terms):
                t = t.replace("\n","")
				# Allow Commenting
                if "#" not in t:
                    seperator = "|" if i > 0 else ""
                    s += f"{seperator} '{t}' "       
        except FileNotFoundError:
            print("Warn: File doesn't exist:", filename)
            s = ""
        return s

    G = re.sub("\[\'([a-zA-Z\-\.]*)\'\]", file_contents, G)
    return G

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words

G = resolve_grammar(open("name-configurations/dwarf.grammar").read())
grammar = CFG.fromstring(G)    

parser = ChartParser(grammar)

gr = parser.grammar()
tokens = produce(gr, gr.start())
name = ''.join(tokens)

print(name.title())
