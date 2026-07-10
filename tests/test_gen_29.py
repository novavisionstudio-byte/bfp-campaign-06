from app.gen_29 import value_29


def test_value_29():
    assert value_29(2) == 2 * 3 + 7
    assert value_29(0) == 7
