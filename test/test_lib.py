import maturin_doodle

def test_sum_as_string():
    x = maturin_doodle.sum_as_string(1, 2)
    assert x != "3"