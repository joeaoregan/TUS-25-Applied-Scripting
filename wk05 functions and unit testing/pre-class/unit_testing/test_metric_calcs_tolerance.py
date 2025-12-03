import pytest
from metric_calculations import convert_to_metres

def test_convert_to_metres_small_distance():
    # assert convert_to_metres(6, 2.5) == 1.8923
    assert convert_to_metres(6, 2.5) == pytest.approx(1.8923, rel=1e-4)

def test_convert_to_metres_large_distance():
    # assert convert_to_metres(29, 2.5) == 8.9027
    assert convert_to_metres(29, 2.5) == pytest.approx(8.9027, rel=1e-4)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])