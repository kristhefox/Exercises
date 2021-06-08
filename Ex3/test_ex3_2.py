import ex1_2
import pytest

@pytest.mark.xfail(strict=True)
def test_ex_1_2_1():
    assert ex1_2.factorial(-1)

def test_ex_1_2_2():
    assert ex1_2.factorial(0)
    assert ex1_2.factorial(1)

@pytest.mark.xfail(strict=True)
def test_ex_1_2_3():
    assert ex1_2.factorial('a','b')
    assert ex1_2.factorial('abracadabra')

def test_ex_1_2_4():
    assert ex1_2.factorial(200)

@pytest.mark.xfail(strict=True)
def test_ex_1_2_5():
    # recursion error
    assert ex1_2.factorial(3100)

