import sys
import os
fp = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.join(fp, '../src/'))
from name_generation.generate import generate, Name, StringToEnum

class Mock():
    def __init__(self):
        pass

def initialize_mock():
    m = Mock()
    m.gender_male = False
    m.gender_female = False
    m.gender_neutral = True
    m.order = Name.NameOrder.Western
    m.origin = Name.Origin.Mountain
    m.namebank = Name.NameBank.Dwarf
    m.has_position = True
    m.verbose = False
    return m

def test_generate_neutral_dwarf_name():
    a = initialize_mock()
    name = generate(a)
    assert(len(name) > 0)

def test_generate_female_dwarf_name():
    a = initialize_mock()
    a.gender_female = True
    name = generate(a)
    assert(len(name) > 0)

def test_string2enum():
    assert(StringToEnum("Dwarf") == Name.NameBank.Dwarf)