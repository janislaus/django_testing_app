import pytest


def test_our_second_test() -> None:
    assert 1 == 1

@pytest.mark.skip
def test_our_first_test() -> None:
    assert 1 == 2

@pytest.mark.skipif(0>1, reason="Skipped because 4>1")
def test_our_third_test() -> None:
    assert 1 == 1

@pytest.mark.xfail
def test_our_four_test() -> None:
    assert 2 == 1


