from parameterized import is_prime
import pytest


@pytest.mark.parametrize("num,expected",[
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (17,True),
    (18,False),
    (19,True),
    (25,False),
])

def test_is_prime(num, expected):
    # assert is_prime(7) == True # insted of this line we created mark.parameterized.
    assert is_prime(num) == expected