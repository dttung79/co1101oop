from function01 import my_max

def test_my_max():
    a = 4
    b = 5
    c = my_max(a, b)
    assert c == 5