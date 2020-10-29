import sys
sys.path.append("..")
from generate import generate, Name


class Mock():
    def __init__(self):
        pass


def test_generate_name():
    a = Mock()
    a.gender_male = True
    a.gender_female = True
    a.gender_neutral = True
    a.order = Name.NameOrder.Western
    a.origin = Name.Origin.Mountain
    a.namebank = Name.NameBank.Dwarf
    a.has_position = True
    generate(a)
