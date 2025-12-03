import pytest
from euro_to_gbp_solutions import convert_euro_to_gbp

def test_convert_euro_to_gbp_passes():
    assert convert_euro_to_gbp(0.1, 0.87) == pytest.approx(0.087)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])