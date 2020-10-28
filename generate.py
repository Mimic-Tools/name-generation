from nltk import CFG
from nltk import ChartParser # parse_cfg, ChartParser
from random import choice
import re
from enum import Enum, auto
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join

class EnumAutoName(Enum):
    # An enum where auto() will default to the enum name
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.value

def get_available_namebanks_and_syllables():
    namebanks = get_available_namebanks()
    syllables = get_available_syllables()
    # return namebanks | syllables   # Nicer 3.9 Python syntax
    return {**namebanks, **syllables}

    
def get_available_syllables(where="syllables"):
    path = "name-segments/"+where
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    available = {}
    for f in onlyfiles:
        f = f.replace(".txt","")
        f = f.replace("-female","")
        f = f.replace("-male","")
        for x in range(10):
            f = f.replace(f"-{x}","")
        f = f.capitalize()
        available[f] = auto()
    return available

def get_available_namebanks(where="forenames"):
    path = "name-segments/"+where
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    available = {}
    for f in onlyfiles:
        f = f.replace(".txt","")
        f = f.replace("-female","")
        f = f.replace("-male","")
        f = f.capitalize()
        available[f] = auto()
    return available

def get_available_origins(where="nouns"):
    path = "name-segments/"+where
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    available = {}
    for f in onlyfiles:
        f = f.replace(".txt","")
        f = f.replace("-female","")
        f = f.replace("-male","")
        f = f.capitalize()
        available[f] = auto()
    return available

class Name:
    class NameOrder(EnumAutoName):
        Eastern = auto()
        Forename_Only = auto()
        Surname_Only = auto()
        Western = "Western"
        
    namebank_values = get_available_namebanks_and_syllables()
    NameBank = EnumAutoName('NameBank', namebank_values)

    origin_values = get_available_origins()
    Origin = EnumAutoName('Origin', origin_values)
        
    class NameType(EnumAutoName):
        Forename = auto()
        Surname = auto()
        
    class Origin(EnumAutoName):
        Aquatic = auto()
        Desert = auto()
        Mountain = auto()
        Tundra = auto()
        Urban = auto()
        Forest = auto()
        Air = auto()
        
    def __init__(self):
        self.gender_male = False
        self.gender_female = False
        self.gender_neutral = False
        
        self.has_position = False
        self.order = Name.NameOrder.Western

class FileFetcher():
    def __init__(self):
        pass
    
    def get_gender_endings(self, config, always_neutral=False):
        e = []
        if config.gender_male:
            e.append("male")
        if config.gender_female:
            e.append("female")
        if config.gender_neutral or always_neutral:
            e.append("")
        if len(e) == 0:
            print("No Gender Selection. Defaulting to gender neutral")
            config.gender_neutral = True
            e.append("")
        return e
    
    def get_position_files(self, config):
        ges = self.get_gender_endings(config)
        pt = []
        for g in ges:
            g = f"-{g}" if g != "" else g
            pt.append(f'prefixes/positions{g}.txt')
         
        return pt

    def SyllableLength(self, namebank):
        path = "name-segments/syllables"
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        unique_syllables = {}
        for f in onlyfiles:
            if namebank in f:
                f = f.replace("-female","")
                f = f.replace("-male","")
                unique_syllables[f] = True
        return len(unique_syllables.items())


class Grammar:
    def __init__(self, config):
        self.config = config
        self.obj = {}
        self.root = "S"
        self.ff = FileFetcher()
        
    def initialize(self):
        self.obj[self.root]= ["PRE", "CORE", "POST"]
        
        self.basic_tokens()

    def basic_tokens(self):
        self.obj["SPC"] = ["' '"]
        self.obj["OF"] = ["'o'", "'f'"]

    def define_position(self, config, optional=False):
        
        # Prefix
        positions = self.ff.get_position_files(config)
        positions = [f"['{p}']" for p in positions]
        self.obj["PRE"] = ["TITLE", "SPC"]
        if optional:
            self.obj["PRE"].append(None)
        
        self.obj["TITLE"] = positions
       
        # Postfix
        origin = config.origin.name.lower()
               
        self.obj["POST"] = ["SPC", "OF", "SPC", "WHERE"]
        if optional:
            self.obj["POST"].append(None)
        # TODO: Allow multiple origins
        self.obj["WHERE"] = [f"['postfixes/{origin}.txt']",]
     
    def setNameOrder(self, order):
        if order == Name.NameOrder.Western:
            self.obj["CORE"] = ["FORENAME", "SPC", "SURNAME"]
        elif order == Name.NameOrder.Eastern:
            self.obj["CORE"] = ["SURNAME", "SPC", "FORENAME"]
        elif order == Name.NameOrder.Forename_Only:
            self.obj["CORE"] = ["FORENAME"]
        elif order == Name.NameOrder.Surname_Only:
            self.obj["CORE"] = ["FORENAME"]
        else:
            print("Unimplemented Name Order: ", order, ". Defaulting to Western")
            self.setNameOrder(Name.NameOrder.Western)

    def getNamesFromSyllables(self, config, name_type):
        ges = self.ff.get_gender_endings(config)
        namebank = config.namebank.name.lower()
        name_type = name_type.name.upper()

        # TODO: Check compatibile with namebanks
        syls = self.ff.SyllableLength(namebank)
        self.obj[name_type] = []
        for x in range(syls):
            self.obj[name_type].append(f"SYLLABLE{x}") 
        
        for x in range(syls):
            pt = []
            for g in ges:
                g = f"-{g}" if g != "" else g
                # TODO: s shouldnt be there.
                pt.append(f'syllables/{namebank}{g}-{x}.txt')
            self.obj[f"SYLLABLE{x}"] = [pt]


    def getNamesFromBank(self, config, name_type):
        ges = self.ff.get_gender_endings(config)
        namebank = config.namebank.name.lower()
        name_type = name_type.name.upper()
        
        pt = []
        for g in ges:
            g = f"-{g}" if g != "" else g
            # TODO: s shouldnt be there.
            pt.append(f'{name_type.lower()}s/{namebank}{g}.txt')
        self.obj[name_type] = [pt]
        
    def constructName(self, config, name_type):
        origin = config.origin.name.lower()
        name_type = name_type.name.upper()
                   
        self.obj[name_type] = ["ADJ", "NOUN"]
        
        self.buildAdjBank(config)
        self.buildNounBank(config)
        
    def buildAdjBank(self, config):
        origin = config.origin.name.lower()
        
        pt = []
        # TODO: Dodginess/Alignment. John Bloodsword seems more evil than John Goldheart
        pt.append(f"['adjectives/{origin}.txt']")
         
        self.obj["ADJ"] = pt
        
    def buildNounBank(self, config):
        origin = config.origin.name.lower()
        
        pt = []
        # TODO: Dodginess/Alignment. John Poisonblood seems more evil than John Goldheart
        pt.append(f"['nouns/{origin}.txt']")
        self.obj["NOUN"] = pt
        
        

    def write(self, filename="custom.grammar"):
        # TODO: order carefully
        s = ""
        for key, value in self.obj.items():
            s += f"{key} -> "
            for i, v in enumerate(value):
                sep = " "
                if v is None:
                    v = " | "
                s += f"{v}{sep}"
            s += "\n"
                
        self.string_repr = s
        f = open(filename, "w")
        f.write(s)
        f.close()
        return filename

    def __str__(self):
        if hasattr(self, "string_repr"):
            return self.string_repr
        else:
            return "Not Finalized"

def define_grammar(config):

    grammar = Grammar(config)
    grammar.initialize()
    if config.has_position:
        grammar.define_position(config)
    grammar.setNameOrder(config.order)

    # Prefer Forenames to be syllable generated
    if grammar.ff.SyllableLength(config.namebank.name.lower()) > 0:
        grammar.getNamesFromSyllables(config, Name.NameType.Forename)
    else:
        grammar.getNamesFromBank(config, Name.NameType.Forename)

    # TODO: Use namebank for Surnames
    grammar.constructName(config, Name.NameType.Surname)
    
    return grammar.write()

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
            print("Warn/Err: File doesn't exist:", filename, ". May produce bad names.")
            s = ""
        return s

    G = re.sub("\[\'([a-zA-Z\-\.\/0-9]*)\'\]", file_contents, G)
    return G

def generate_name(G):
    grammar = CFG.fromstring(G)    

    parser = ChartParser(grammar)

    gr = parser.grammar()
    tokens = produce(gr, gr.start())
    name = ''.join(tokens)
    return name.title()

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


def generate(args):
    config = Name()
    config.has_position = True
    config.origin = args.origin
    config.namebank = args.namebank
    config.order = args.order
    config.gender_male = args.gender_male
    config.gender_female = args.gender_female
    config.gender_neutral = args.gender_neutral
    grammar_file = define_grammar(config)

    G = resolve_grammar(open(grammar_file).read())
    name = generate_name(G)

    print("Your Character:", name)

def parse_args():
    ap = ArgumentParser(description="Generate a character name")

    # Gender
    ap.add_argument('--gender-male', action="store_true")
    ap.add_argument('--gender-female', action="store_true")
    ap.add_argument('--gender-neutral', action="store_true")
       
    # Origins
    ap.add_argument('--order', type=Name.NameOrder, choices=list(Name.NameOrder), nargs="?", default=Name.NameOrder.Western)
    ap.add_argument('--origin', type=Name.Origin, choices=list(Name.Origin), nargs="?", default=Name.Origin.Mountain)
    ap.add_argument('--namebank', type=Name.NameBank, choices=Name.NameBank, nargs="?", default=Name.NameBank.Dwarf)
    args = ap.parse_args()
    return args
    

if __name__ == "__main__":
    a = parse_args()
    generate(a)
