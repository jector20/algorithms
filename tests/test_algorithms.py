import pytest
from algorithms.search import index, fibonacci_number

def test_search_sequence():
    assert list(fibonacci_number(1, 5)) == [(1, -1), (2, 1), (3, 2), (4, 3)]

@pytest.mark.parametrize('array_1', [[10]])
def test_search_array_1(array_1):
    assert index(array_1, 9) ==  -1
    assert index(array_1, 10) ==  0
    assert index(array_1, 11) ==  -1
        
        
@pytest.mark.parametrize('array_2', [[10, 20]])
def test_search_array_2(array_2):
    assert index(array_2, 9) ==  -1
    assert index(array_2, 10) ==  0
    assert index(array_2, 11) ==  -1
    assert index(array_2, 20) ==   1
    assert index(array_2, 21) ==  -1
        
@pytest.mark.parametrize('array_9',  [[11, 21, 33, 34, 36, 47, 48, 59, 610]])
def test_search_array_9(array_9):
        
    assert index(array_9, 11) == 0
    assert index(array_9, 21) == 1
    assert index(array_9, 33) == 2
    assert index(array_9, 59) == 7
    assert index(array_9, 610) == 8

    assert index(array_9, 609) == -1
    assert index(array_9, 10) == -1