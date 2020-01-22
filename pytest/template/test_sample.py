# content of test_sample.py
import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5

if __name__ == "__main__":
    pytest.main('-q test_sample.py')
