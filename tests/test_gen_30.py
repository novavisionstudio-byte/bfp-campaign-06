from app.gen_30 import value_30


def test_value_30():
    assert value_30(2) == 2 * 3 + 8
    assert value_30(0) == 8
