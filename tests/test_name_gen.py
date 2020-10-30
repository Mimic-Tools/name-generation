import sys
import os
fp = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.join(fp, '../src/name_generation'))
from src.name_generation.generate import generate, Name

class Mock():
    def __init__(self):
        pass


def test_generate_neutral_dwarf_name():
    a = Mock()
    a.gender_male = False
    a.gender_female = False
    a.gender_neutral = True
    a.order = Name.NameOrder.Western
    a.origin = Name.Origin.Mountain
    a.namebank = Name.NameBank.Dwarf
    a.has_position = True
    generate(a)

def test_generate_female_dwarf_name():
    a = Mock()
    a.gender_male = False
    a.gender_female = True
    a.gender_neutral = True
    a.order = Name.NameOrder.Western
    a.origin = Name.Origin.Mountain
    a.namebank = Name.NameBank.Dwarf
    a.has_position = True
    generate(a)
