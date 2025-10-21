import maturin_doodle

def test_sum_as_string():
    assert maturin_doodle.sum_as_string(1, 2) == "5"
    assert maturin_doodle.sum_as_string(3, 4) == "7"