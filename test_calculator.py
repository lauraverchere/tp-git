from calculator import addition, soustraction, division

def test_addition():
    assert addition(1, 2) == 3
    
def test_substraction() : 
    assert soustraction (3,1) == 2