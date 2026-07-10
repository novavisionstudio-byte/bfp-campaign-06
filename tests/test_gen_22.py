from app.gen_22 import value_22


def test_value_22():
    assert value_22(2) == 2 * 7 + 6
    assert value_22(0) == 6
