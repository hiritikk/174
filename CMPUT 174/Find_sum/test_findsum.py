#test
from find_sum import add_number

def test_if_list_empty():
    assert add_number([]) == None       #imp quiz 3
    
def test_if_not_list():
    assert add_number(2) == None

def test_all_positives():
    assert add_number([2,4,6]) == 12

def test_all_negatives():
    assert add_number([-2,-4,-6]) == -12

def test_positives_negatives():
    assert add_number([-2,4,6]) == 8

def test_number_not_int():
    assert add_number([2,3,'a']) == None
    
    