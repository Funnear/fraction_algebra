import pytest

from fraction.fraction import Fraction


class TestInitiation:

    @pytest.mark.parametrize("fraction, expected_result", [
        (Fraction(0, 1), 0.0),
        (Fraction(8, 4), 2.0),
        (Fraction(1, 1000), 0.001),
        (Fraction(1, 3), 0.3333333333333333),
        (Fraction(11, 3), 3.6666666666666665),
        (Fraction(-1, 2), -0.5),
        ])
    def test_convert_to_float(self, fraction, expected_result):
        result = float(fraction)
        assert result == expected_result

    @pytest.mark.parametrize("fraction, expected_result", [
        (Fraction(0, 1), 0),
        (Fraction(8, 4), 2),
        (Fraction(1, 1000), 0),
        (Fraction(11, 3), 3),
        (Fraction(-8, 7), -1),
        (Fraction(8, 7), 1),
    ])
    def test_convert_to_int(self, fraction, expected_result):
        result = int(fraction)
        assert result == expected_result
