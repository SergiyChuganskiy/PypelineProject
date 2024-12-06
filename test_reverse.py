'''it is code for testing our naib program'''
from main import str_reverse

def test_reverse_1():
    '''first test'''
    assert str_reverse("boom") == "moob"

def test_reverse_2():
    '''second test'''
    assert str_reverse(" a b c d e f") == "f e d c b a "
