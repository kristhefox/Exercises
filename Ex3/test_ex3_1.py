import ex1_1
import pytest

@pytest.mark.xfail(strict=True)
def test_ex1_1_1():
    assert ex1_1.minmax([])

def test_ex1_1_2():
    assert ex1_1.minmax([0])
    assert ex1_1.minmax([421,2131232,33,42312,5,423232,21])
    assert ex1_1.minmax([23213123123123,246524,1233253235,46546123,3446574,12465723,434324,6932829,634])

def test_ex1_1_3():
    assert ex1_1.minmax(['a','b','c','y','s','w','n'])

def test_ex1_1_4():
    assert ex1_1.minmax(['alpha','beta','gamma','delta'])

def test_ex1_1_5():
    assert ex1_1.minmax([2<4])
    assert ex1_1.minmax([2<=4])
    assert ex1_1.minmax([100>50>25])